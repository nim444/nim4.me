from django.db import models


class Bookmarks(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField()
    date = models.DateField(auto_now=False, auto_now_add=False)

    # __ Show in String __
    def __str__(self):
        return self.title


class Playlists(models.Model):
    title= models.CharField( max_length=200)
    link = models.URLField()
    date = models.DateField(auto_now=False, auto_now_add=False)

    # __ Show in String __
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=80)
    body = models.TextField()
    link = models.URLField(null=True,blank=True)
    pic = models.ImageField(upload_to='portfolio/',blank=True,null=True)

    def __str__(self):
        return self.title


class ContactForm(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=16, blank=True, null=True)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.email


class FileUpload(models.Model):
    title = models.CharField(max_length=128)
    fileupload = models.FileField(upload_to='fileupload/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "fileupload/%s" % self.fileupload


