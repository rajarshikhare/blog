from django.contrib import admin

# Register your models here.
from .models import Topic, Author, Comment, Client

admin.site.register(Topic)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Client)