from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404,redirect
import paydunya
from paydunya import InvoiceItem, Store, Invoice
from orders.models import Order
from django.conf import settings 

paydunya.debug = True

paydunya.api_keys = settings.PAYDUNYA_ACCESS_TOKENS

store = Store(name='Magasin Chez Jaba')


def payment_process(request):
    try:
        if not isinstance(request, HttpRequest):
            request = HttpRequest()
        order_id = request.session.get("order_id")
        order = get_object_or_404(Order, pk=order_id)
        order_items = order.items.all()
        items = [InvoiceItem(
            name=item.product.name,
            quantity=item.quantity,
            unit_price=str(item.price),
            total_price=str(item.price * item.quantity),
            description=item.product.name
        ) for item in order_items
        ]
        invoice = paydunya.Invoice(store)
        host = request.get_host()
        invoice.callback_url = f"http://{host}/payment-done/"
        invoice.cancel_url = f"http://{host}/payment-canceled/"
        invoice.return_url = f"http://{host}/payment-done/"
        invoice.add_items(items)
        successful, response = invoice.create()
        print(response)
        if successful:
            print(response)
            return redirect(response.get("response_text"))
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return HttpResponse("<h2>Votre commande a etait envoyer,nous vous contacterons pour plus de details </h2> ")


def payment_done(request):
    token = request.GET.get("token")
    invoice = Invoice(store)
    successful, response = invoice.confirm(token)
    if successful:
        return HttpResponse("<h2>Merci pour le paiement</h2>")


def payment_canceled(request):
    return HttpResponse("<h2>Vous avez annulé le paiement</h2>")