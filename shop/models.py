from django.db import models
from django.urls import reverse
from django.conf import settings

               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            |||||||#######_____-----_____-----Notre model de contenue  est defini ici -----_____-----_____######|||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural ="categories"


    


class Product(models.Model):
    category = models.ForeignKey(
     Category, related_name="products",on_delete=models.
     CASCADE,)
    name =models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to="products/%Y/%m%d",)
    description = models.TextField(blank=True)
    info_produit = models.TextField(blank=True)
    fabriquant = models.TextField(blank=True)
    price =  models.DecimalField(max_digits=20,decimal_places=0)
    availaible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def get_absolute_url(self):
        
        return reverse("product-details", kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
    
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author.username + ' - ' + str(self.date)
