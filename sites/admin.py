from django.contrib import admin

# Register your models here.
from sites.models import Site, Like

admin.site.register(Site)
admin.site.register(Like)

