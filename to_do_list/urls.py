from django.urls import path, include
from to_do_list import views
from .views import TasksList, TaskDetail, TaskCreate, TaskEdit, TaskDelete


urlpatterns = [
    path('', TasksList.as_view(), name='list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('edit/<int:pk>/', TaskEdit.as_view(), name='edit'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='delete'),
]