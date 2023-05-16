from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/category")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/gallery")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/company")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Country(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/country")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
