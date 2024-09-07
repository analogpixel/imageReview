from django.shortcuts import render
from .models import Tag,Image,Day
from django.http import HttpResponse, FileResponse, JsonResponse
from django.conf import settings
from .scanfiles import scanfiles
import mimetypes
import os
import random
from django.views.decorators.csrf import csrf_exempt
import datetime

def serve_image(request, file_name):
    image_path = os.path.join(settings.IMAGES_DIR, file_name)
    content_type, _ = mimetypes.guess_type(image_path)

    if content_type is None:
        content_type = 'application/octet-stream'

    return FileResponse(open(image_path, 'rb'), content_type=content_type)

@csrf_exempt
def del_tag(request, file_name):
    if request.method == 'POST':
        img = Image.objects.get(file_name=file_name)
        tag_name = request.POST.get('tag')
        print("removing tag", tag_name)
        tag = Tag.objects.get(name=tag_name)
        img.tags.remove(tag)
        img.save()
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False})

@csrf_exempt
def add_tag(request, file_name):
    if request.method == 'POST':
        img = Image.objects.get(file_name=file_name)
        tag_name = request.POST.get('tag')
        print("adding tag", tag_name)
        tag, _ = Tag.objects.get_or_create(name=tag_name)
        img.tags.add(tag)
        img.save()
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False})

@csrf_exempt
def update_note(request, file_name):
    if request.method == 'POST':
        img = Image.objects.get(file_name=file_name)
        img.notes = notes = request.POST.get('note')
        img.save()
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False})

def update_star(request, file_name):
    img = Image.objects.get(file_name=file_name)
    img.stared = not img.stared
    img.save()
    return JsonResponse({'status':img.stared})

def index(request, review_date=None):
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/

     
    # search Day for todays date and then return images
    # if not found create a new Day
    if review_date:
        current_date = datetime.datetime.strptime(review_date, '%Y-%m-%d')
    else:
        current_date = datetime.date.today()

    day = Day.objects.filter(date=current_date)

    if not day:
        print("no day found creating")
        day = Day(date=current_date)
        day.save()

        _images = Image.objects.all().order_by("?")
        images = _images[0:4]
        for i in images:
            print("adding image", i)
            day.images.add(i)
    else:
        print("day found")
        print(day[0].images)
        day = day[0]

    images = day.images.all()
    print("images:", images)

    return render(request, 'review_app/index.html', 
                  {'images': images, 
                   'yesterday': (current_date - datetime.timedelta(days=1)).strftime('%Y-%m-%d'), 
                   'tomorrow': (current_date + datetime.timedelta(days=1)).strftime('%Y-%m-%d'),
                   'today': datetime.date.today().strftime('%Y-%m-%d')}
                  )

def tag_page(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    # search for all images that have this tag
    images = Image.objects.filter(tags=tag)
    return render(request, 'review_app/tag.html', {'images': images, 'tag': tag})

def star_page(request):
    images = Image.objects.filter(stared=True)
    return render(request, 'review_app/star.html', {'images': images})

# reindex all the images
def rescan(request):
    # add new from fs
    for f in scanfiles(settings.IMAGES_DIR):
        # if filename has extension in list of extensions settings.IMAGES_EXTENSIONS
        # then add to db
        _, ext = os.path.splitext(f)
        if ext.lower() in settings.IMAGES_EXTENSIONS:
            Image.objects.get_or_create(file_name=f)

    # remove files in db but not fs

    return HttpResponse("scanned")

