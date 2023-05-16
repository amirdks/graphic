from django.shortcuts import render
from django.views import View
from .models import *


# Create your views here.
class IndexView(View):
    def get(self, request):
        gallery_images = GalleryImage.objects.all()
        categories = Category.objects.all()
        countries = Country.objects.all()
        companies = Company.objects.all()
        context = {
            "gallery_images": gallery_images,
            "categories": categories,
            "countries": countries,
            "companies": companies,
        }
        return render(request, 'main_module/home.html', context)
