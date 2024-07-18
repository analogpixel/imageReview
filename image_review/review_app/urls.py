from django.urls import path
from . import views

urlpatterns = [
    path('img/<str:file_name>', views.serve_image, name='serve_image'),
    path('update_note/<str:file_name>', views.update_note, name='serve_image'),
    path('update_star/<str:file_name>', views.update_star, name='serve_image'),
    path('rescan/', views.rescan, name='test'),
    path('', views.index, name='index'),
]


