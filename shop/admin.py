from django.contrib import admin
from .models import Category, Product

#Les models du categorie et du produit sont enregistrés ci dessous ! 

admin.site.site_header = "DEEL_BII"
admin.site.site_title = "Boutique Deel bii"
admin.site.index_title ="Direction du site"




admin.site.register(Category)
admin.site.register(Product)