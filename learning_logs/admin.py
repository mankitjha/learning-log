from django.contrib import admin

from .models import Topic, Entry

# Registering model.
admin.site.register(Topic)
admin.site.register(Entry)

