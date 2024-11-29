from django.urls import path
from journal import views
from .views import EntryList, CreateEntry, ViewEntry, EditEntry

urlpatterns = [
    path('', EntryList.as_view(), name='entry'),
    path('add/', CreateEntry.as_view(), name='add_entry'),
    path('view/<int:pk>/', ViewEntry.as_view(), name='view_entry'),
    path('edit/<int:pk>/', EditEntry.as_view(), name='edit_entry'),
]