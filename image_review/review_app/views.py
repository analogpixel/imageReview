from django.shortcuts import render
from . import models

# Create your views here.
def test(request):
    # Creating tags
    tag1 = Tag.objects.create(name='Electronics')
    tag2 = Tag.objects.create(name='Gadgets')

    # Creating an item
    item = Image.objects.create(file_name='test_file.jpg')

    # Adding tags to the item
    item.tags.add(tag1, tag2)

    # Accessing tags of an item
    item_tags = item.tags.all()

    # Accessing items of a tag
    tag_items = tag1.items.all()
