from django.urls import path, include
from album import views


urlpatterns = [
    path('', views.home_page, name='all'),
    path('add/', views.addPics, name='add_photo'),
    path('view/<int:pk>', views.viewPics, name='view_photo'),
    path('delete/<int:pk>', views.deletePics, name='delete_photo'),
]
