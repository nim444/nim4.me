from django.db import models


class Library(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=False, auto_now=False)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/library/{}/".format(self.slug)