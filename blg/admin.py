from django.contrib import admin

# Register your models here.
from .models import Topic, Author, Comment

admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Comment)