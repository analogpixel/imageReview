from django.shortcuts import render
from .models import Tag,Image
from django.http import HttpResponse, FileResponse, JsonResponse
from django.conf import settings
from .scanfiles import scanfiles
import mimetypes
import os
import random
from django.views.decorators.csrf import csrf_exempt

def serve_image(request, file_name):
    image_path = os.path.join(settings.IMAGES_DIR, file_name)
    content_type, _ = mimetypes.guess_type(image_path)

    if content_type is None:
        content_type = 'application/octet-stream'

    return FileResponse(open(image_path, 'rb'), content_type=content_type)

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

def index(request):
    # https://docs.djangoproject.com/en/5.0/ref/models/querysets/
    _images = Image.objects.all().order_by("?")
    images = _images[0:4]
    return render(request, 'review_app/index.html', {'images': images})

# reindex all the images
def rescan(request):
    # add new from fs
    for f in scanfiles(settings.IMAGES_DIR):
        Image.objects.get_or_create(file_name=f)

    # remove files in db but not fs

    return HttpResponse("scanned")

