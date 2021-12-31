from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.contrib import messages
from .models import Bookmarks, Playlists, Project, ContactForm
from django.utils import timezone


def error_404_view(request,exception):
    return render(request,'app/404.html')


class HomeView(TemplateView):
    template_name='app/index-v2.html'


class BookmarksListView(ListView):
    model = Bookmarks
    paginate_by = '20'
    queryset = Bookmarks.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookmarksSearchView(ListView):

    model = Bookmarks
    paginate_by = '20'
    queryset = Bookmarks.objects.all().order_by('-date')

    def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                bookmarks_list = self.model.objects.filter(title__icontains=query)
            else:
                bookmarks_list = self.model.objects.all()
            return bookmarks_list


class PlaylistsListView(ListView):
    model = Playlists
    paginate_by = '20'
    queryset = Playlists.objects.all().order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PlaylistsSearchView(ListView):

    model = Playlists
    paginate_by = '20'
    queryset = Playlists.objects.all().order_by('-date')

    def get_queryset(self):
            query = self.request.GET.get('q')
            if query:
                playlists_list = self.model.objects.filter(title__icontains=query)
            else:
                playlists_list = self.model.objects.all()
            return playlists_list


class FormPageView(View):
    def get(self, request):
        return render(request, 'app/hello.html', {})

    def post(self, request):
        fields = ['full_name', 'email', 'phone', 'message']
        kwargs = {}

        for field in fields:
            if field not in request.POST or request.POST[field] == '':
                messages.error(request, 'Please enter {}'.format(field))
                return self.get(request)
            kwargs[field] = request.POST.get(field)
        ContactForm.objects.create(**kwargs)

        messages.success(request, 'Your message has been submitted')
        return self.get(request)

