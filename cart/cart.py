"""
from shop.models import Product
from django.conf import settings
from decimal import Decimal


# initialisation du panier 
class Cart(object):
    def __init__(self, request):

        self.session = request.session
        cart =self.session.get(settings.CARTE_SESSION_ID)
        if not cart :
            cart= self.session[settings.CARTE_SESSION_ID] = {}
        self.cart = cart    
    def save(self):
         self.session.modified = True
        

# Ajout au panier 

    def add(self, product, quantity=1,override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]= {"quantity":0, "price": str(product.price)}
        if override_quantity:
                self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity      
        self.save()

# Supprimer du panier 

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()     

# Récupérer les éléments

    ### 
    def __iter__(self):    
            product_ids = self.cart.keys()
            products = Product.objects.filter(id__in= product_ids)
            cart = self.cart.copy()


            for product in products:
                cart[str(product.id)]["product"] =product

            for item in cart.values():
                item["price"] = Decimal(item['price'])
                item["total_price"] = Decimal(item['price']) * item['quantity']
                yield item
#Compter les éléments présent dans le panier 

    ###
    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
            
#Calculer la somme total du panier

    ###
    def get_total_price(self):
        return sum(Decimal(item["price"] * item["quantity"]) for item in self.cart.values())
            
 # Vider le panier 
    ###
    def clear(self):
        del self.session[settings.CARTE_SESSION_ID]
        self.save()
"""


from shop.models import Product
from django.conf import settings
from decimal import Decimal


               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            |||||||#######_____-----_____-----Notre panier est initialiser ici-----_____-----_____######|||||| |||||
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 



class Cart(object):
    def __init__(self, request):

        self.session = request.session
        cart =self.session.get(settings.CARTE_SESSION_ID)
        if not cart :
            cart= self.session[settings.CARTE_SESSION_ID] = {}
        self.cart = cart    
    def save(self):
         self.session.modified = True
        


# Ajout au panier 

    def add(self, product, quantity=1,override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]= {"quantity":0, "price": str(product.price)}
        if override_quantity:
                self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity      
        self.save()

# Supprimer du panier 

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()     

# Récupérer les éléments

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in= product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] =product

        for item in cart.values():
            item["price"] = Decimal(item['price'])
            item["total_price"] = Decimal(item['price']) * item['quantity']
            yield item

#Compter les éléments présent dans le panier 

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())
            
#Calculer la somme total du panier

    def get_total_price(self):
        return sum(Decimal(item["price"] )* item["quantity"] for item in self.cart.values())
            
 # Vider le panier 
    def clear(self):
        del self.session[settings.CARTE_SESSION_ID]
        self.save()
