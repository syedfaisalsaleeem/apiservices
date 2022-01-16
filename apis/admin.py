from django.contrib import admin

# Register your models here.
from .models import Document, Folder, Topic
admin.site.register(Document)
admin.site.register(Folder)
admin.site.register(Topic)