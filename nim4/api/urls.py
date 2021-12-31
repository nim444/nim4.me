from django.conf.urls import url, include, re_path
from rest_framework import routers
from .serializers import BookmarksViewSet, PlaylistsViewSet, LibraryViewSet




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'bookmarks', BookmarksViewSet)
router.register(r'playists', PlaylistsViewSet)
router.register(r'library', LibraryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls)),
]