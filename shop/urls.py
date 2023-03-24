from django.urls import path
from . import views
#from .views import category
from shop.views import ProductList,index, ProductDetail
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="home"),
    path("contact/", views.contact, name="contact"), 
    path('category/', views.category, name='category'),
    path("shop/", ProductList.as_view(), name='product-list'),
    path("shop/<slug:slug>/details/", ProductDetail.as_view(), name="product-details"), 

    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)