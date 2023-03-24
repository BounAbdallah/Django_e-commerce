from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def send_new_order_mail(email):
    send_mail(
    'Votre commande sur le site Deal Bii ',
    "Bonjour Mr/Mrs, suite a votre comande sur le site Deal Bii , nous vous informons que votre commande a ete bien reussi votre marchandise vous sera livrer d'ici peu. Merci de votre fidelite !",
    'dealbii@contact.com',
    [email],
    fail_silently=False,
    )


# envoi du mail avectemplate 
def send_new_order_mail_with_template(email):
    template = get_template("email/new-order.html")
    context ={"email": email}
    subject, from_email = ("Votre commande sur DealBii","dealbii@contact.com")
    body = template.render(context)
    message = EmailMultiAlternatives(subject,body,from_email,[email])
    message.attach_alternative(body, "text/html")
    message.send(fail_silently=False)


def payement_successfull_email(email):
    send_mail(
    'Votre commande sur le site Deal Bii ',
    "Bonjour Mr/Mrs, nous vous informons que nous avons bien reçu votre paiement !",
    'dealbii@contact.com',
    [email],
    fail_silently=False,
    )