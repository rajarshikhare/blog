from django.contrib import admin

# Register your models here.
from .models import Topic, Author

admin.site.register(Topic)
admin.site.register(Author)