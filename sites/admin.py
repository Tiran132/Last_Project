from django.contrib import admin

# Register your models here.
from sites.models import Site, Likes

admin.site.register(Site)
admin.site.register(Likes)

