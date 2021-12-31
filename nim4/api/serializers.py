from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from app.models import Bookmarks, Playlists
from library.models import Library

# Serializers define the API representation.
class BookmarksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmarks
        fields = ['title','link','date']


    # # ViewSets define the view behavior.
class BookmarksViewSet(viewsets.ModelViewSet):
    queryset = Bookmarks.objects.all().order_by('-date')
    serializer_class = BookmarksSerializer

# Serializers define the API representation.
class PlaylistsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlists
        fields = ['title','link','date']


# # ViewSets define the view behavior.
class PlaylistsViewSet(viewsets.ModelViewSet):
    queryset = Playlists.objects.all().order_by('-date')
    serializer_class = PlaylistsSerializer


# Serializers define the API representation.
class LibrarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'



# # ViewSets define the view behavior.
class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
