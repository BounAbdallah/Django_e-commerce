from django.shortcuts import get_object_or_404, redirect, render
from shop.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from cart.forms import CarteAddProductForm



               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #           |||||||#######_____-----_____-----La suppression du panier  est defini ici -----_____-----_____######|||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 

@require_POST
def cart_remove(request, product_id):
    cart =Cart(request)
    product = get_object_or_404(Product, id = product_id)
    cart.remove(product)
    return redirect("cart_detail")


               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            |||||||#######_____-----_____-----L'ajout au panier est defini ici -----_____-----_____######|||||||||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 

@require_POST
def cart_add(request, product_id):
    cart =Cart(request) 
    product =get_object_or_404(Product, id = product_id)
    form = CarteAddProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product = product, quantity = cleaned_data["quantity"],
        override_quantity = cleaned_data["override"])
    return redirect("cart_detail") 
    

               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            |||||||#######_____-----_____-----Le details de la cart est defini ici -----_____-----_____######|||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 

def cart_detail(request):
    cart =Cart(request)
    for item in cart:
        item['update_quantity_form'] = CarteAddProductForm(initial={"quantity": item["quantity"], "override": True})
    return render(request, "cart/cart_detail.html", {"cart": cart})    