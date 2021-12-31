from django.urls import path
from .views import LibraryListView, LibraryDetailView, LibrarySearchView
from django.contrib.auth.decorators import login_required, permission_required


app_name= 'library'

urlpatterns = [
    path('library', LibraryListView.as_view(), name='library'),
    path('library/<slug:slug>/', LibraryDetailView.as_view(), name='library-detail'),
    path('library/search', LibrarySearchView.as_view(), name='searchlibrary'),
]