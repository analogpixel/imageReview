from django.shortcuts import render
from .models import Tag,Image
from django.http import HttpResponse
from .scanfiles import scanfiles

def index(request):
    images = Image.objects.all()
    return render(request, 'review_app/index.html', {'images': images})

# reindex all the images
def rescan(request):
    # add new from fs
    for f in scanfiles("~/imageReview/sample_images"):
        Image.objects.get_or_create(file_name=f)

    # remove files in db but not fs

    return HttpResponse("scanned")

# Create your views here.
def test(request):
    # Creating tags
    # Attempt to get or create the object
    tag1, created = Tag.objects.get_or_create( name='Electronics')
    tag2, created = Tag.objects.get_or_create( name='Gadgets')

    # Creating an item
    item,created = Image.objects.get_or_create(file_name='test_file.jpg')

    # Adding tags to the item
    item.tags.add(tag1, tag2)

    # Accessing tags of an item
    item_tags = item.tags.all()

    # Accessing items of a tag
    tag_items = tag1.items.all()

    return HttpResponse("ok")
