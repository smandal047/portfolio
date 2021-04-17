from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, default='Project Title')
    short_description = models.CharField(max_length=100, default='A short description')
    technology = models.CharField(max_length=20, default='Python')
    image = models.TextField(null=True)
    github_link = models.TextField(null=True)

    def __str__(self):
        return f'{self.title}, {self.short_description}'


class Post(models.Model):
    post_title = models.CharField(max_length=255, default='Post Title')
    body = models.TextField(default='Body of the post, add image using <img> tag')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    related_project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title

    class Meta:
        ordering = ['post_title']
