from django.urls import path
from . import views

urlpatterns = [
    path('img/<str:file_name>', views.serve_image, name='serve_image'),
    path('test/', views.test, name='test'),
    path('rescan/', views.rescan, name='test'),
    path('', views.index, name='index'),
]


