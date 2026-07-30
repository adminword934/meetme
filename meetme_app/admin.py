from django.contrib import admin
from .models import Celebrity, Package, WebsiteSettings

admin.site.register(Celebrity)
admin.site.register(Package)
admin.site.register(WebsiteSettings)