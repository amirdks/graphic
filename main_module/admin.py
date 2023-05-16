from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(GalleryImage)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Company)
