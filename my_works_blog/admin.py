from django.contrib import admin
from my_works_blog.models import Project, Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, PostAdmin)
admin.site.register(Post, CategoryAdmin)
