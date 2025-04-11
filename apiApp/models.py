from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
     
    email = models.EmailField(unique=True)
    profile_picture_url = models.URLField(blank=True, null=True)

    def __str__(self):
	    return self.email
 
 
class Category(models.Model):
    name= models.CharField(max_length=255)
    slug= models.SlugField(unique=True)
    image= models.ImageField( upload_to="category_img",blank=True, null=True)
    
    def __str__(self):
        return self.name
 
 
class Product(models.Model):
    name= models.CharField(max_length=255),
    description= models.TextField(),
    price= models.DecimalField(max_digits=10, decimal_places=2),
    slug= models.SlugField(unique=True, blank=True)
    image= models.ImageField( upload_to="product_img",blank=True, null=True)
    featured= models.BooleanField(default=False)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="products", null=True, blank=True)
    
    
    def __str__(self):
        return self.name
 
    