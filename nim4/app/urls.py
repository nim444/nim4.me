from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView , BookmarksListView, BookmarksSearchView, PlaylistsListView, PlaylistsSearchView, FormPageView

namespace='app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('bookmarks/', BookmarksListView.as_view(), name='bookmarks'),
    path('bookmarks/search', BookmarksSearchView.as_view(), name='searchbookmarks'),
    path('playlists/', PlaylistsListView.as_view(), name='playlists'),
    path('playlists/search', PlaylistsSearchView.as_view(), name='searchplaylists' ),
    path('hello',FormPageView.as_view(), name='hello'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)