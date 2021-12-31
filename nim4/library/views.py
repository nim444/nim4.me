from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Library
# +++ import Utils +++
from django.utils import timezone
from django.contrib.auth.decorators import login_required



class LibraryListView(ListView):
    model = Library
    paginate_by = '20'
    queryset = Library.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LibraryDetailView(DetailView):
    model = Library

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class LibrarySearchView(ListView):

    model = Library
    paginate_by = '20'
    queryset = Library.objects.all().order_by('-date')

    def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                library_list = self.model.objects.filter(title__icontains=query)
            else:
                library_list = self.model.objects.all()
            return library_list