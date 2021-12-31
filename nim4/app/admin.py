from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from .models import Bookmarks, Playlists, Project, ContactForm, FileUpload

admin.site.site_header = 'Nim4 | backoffice'


class BookmarksAdmin(ImportExportActionModelAdmin):

    list_display=['title','date']
    search_fields=['title']
    list_filter=['date']

    class Meta:
        model = Bookmarks


admin.site.register(Bookmarks,BookmarksAdmin)


class PlaylistsAdmin(ImportExportActionModelAdmin):
    
    list_display=['title','date']
    search_fields=['title']
    list_filter=['date']


    class Meta:
        model = Playlists


admin.site.register(Playlists,PlaylistsAdmin)


class ContactFormAdmin(ImportExportActionModelAdmin):
    list_display = ['full_name','email','phone','date']


admin.site.register(ContactForm,ContactFormAdmin)


class FileUploadAdmin(ImportExportActionModelAdmin):
    list_display = ['title','fileupload']


admin.site.register(FileUpload, FileUploadAdmin)