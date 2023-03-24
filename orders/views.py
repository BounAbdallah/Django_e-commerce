from django.shortcuts import render, redirect

from drams.send_mail.views import send_new_order_mail_with_template
from .forms import OrderCreateForm
from cart.cart import Cart
from .models import OrderItem, Order


def Order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            email = form.cleaned_data.get("email")
            for item in cart:
                OrderItem.objects.create(
                    order =order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            request.session["order_id"] = order.id 

            #Envoyer un mail de confirmation au client 
            send_new_order_mail_with_template(email)
        return redirect("payment-process")
            
    else :
        form =OrderCreateForm()
        return render(request, "orders/create.html", {"cart":cart, "form":form, })       

def Order_created(request):
    return render(request, "orders/created.html")
def updating(request):
    order = Order.objects.all()
    return render(request,{"order":order})

    