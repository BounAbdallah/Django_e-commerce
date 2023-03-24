from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Q 
from cart.forms import CarteAddProductForm
from django.views.generic import DetailView,View





               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            ||||||||######## _____-----_____-----Definition de la page d'acceuil-----_____-----_____ ##########|||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 



template_name = "shop/index.html"
def index(request):

    products = Product.objects.all()

    context = {"products": products,}
    return render(request, "index.html", context,  )

def contact(request):
    return render(request,"contact.html")

 






def category(request):
    categories = Category.objects.all()
   
    return render(request, 'categories.html', {'categories': categories})


               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            ||||||||######## _____-----_____-----Fonction de liste de produits-----_____-----_____ ##########|||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\########## 
    
class ProductList(View):
        template_name = "shop/product_list.html"

        def get(self, request):
            products = Product.objects.all()
            categories = Category.objects.all()
            q = request.GET.get("q")
            if q:
              products = Product.objects.filter(
                Q(name__icontains=q)| 
                Q(description__icontains=q)|
                Q(price__icontains=q)|
                Q(category__name__icontains=q))
            print("Query", q)
            return render(request,self.template_name, {"products": products, "categories": categories})

               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
  #            ||||||||######## _____-----_____-----Fonction de details de produits-----_____-----_____ ##########|||||| 
               ########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########  






class ProductDetail(DetailView):
    model = Product
    template_name = "shop/product_details.html"
    
    def get_context_data(self, **kwargs):
        context = super( ProductDetail, self).get_context_data(**kwargs)
        context["cart_product_form"] = CarteAddProductForm()
        return context

########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
######## _____-----_____-----La pagination de la page de liste de produits-----_____-----_____ ########## 
########/////////////////////|||||||||||||||||||||||||||||||||||||||||||||\\\\\\\\\\\\\\\\\\\\\##########
    

from django.shortcuts import render, get_object_or_404
from .models import Product, Comment

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    comments = Comment.objects.filter(product=product).order_by('-created_at')
    context = {
        'product': product,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)
