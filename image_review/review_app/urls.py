from django.urls import path
from . import views

urlpatterns = [
    path('img/<str:file_name>', views.serve_image, name='serve_image'),
    path('update_note/<str:file_name>', views.update_note, name='update_note'),
    path('update_star/<str:file_name>', views.update_star, name='update_star'),
    path('add_tag/<str:file_name>', views.add_tag, name='add_tag'),
    path('del_tag/<str:file_name>', views.del_tag, name='del_tag'),
    path('rescan/', views.rescan, name='rescan'),
    path('', views.index, name='index'),
]


