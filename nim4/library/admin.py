from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportActionModelAdmin

from .models import Library


class LibraryAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    list_display = ['title','date' ]

    summernote_fields = ('body')

    class Meta:
        model = Library


admin.site.register(Library, LibraryAdmin)

