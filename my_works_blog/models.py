from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, default='Project Title')
    short_description = models.CharField(max_length=100, default='A short description')
    technology = models.CharField(max_length=20, default='Python')
    image = models.TextField(default='\images\coding_screen_banner.jpg')
    github_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.short_description}'


class Post(models.Model):
    post_title = models.CharField(max_length=255, default='Post Title')
    # body = models.TextField(default='Body of the post, add image using <img> tag')
    body = RichTextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ['post_title']
