from django.shortcuts import render
from django.http import HttpResponse
from .models import Products, Store, Category

# Create your views here.

def index(request, id):
    print(request.method, id)
    return HttpResponse('Home Papthge')


"""def web_page(products):
    page = '<ul>'
    for product in products:
        page +=f"<li><h1>{product['name']}</h1><h2>{product['desc']}</h2><p>{product['price']}</p</li>"
    page +='<ul>'
    return page

def store_page(stores):
    page = '<ul>'
    for store in stores:
        page +=f"<li><h1>{store.name}</h1><h2>{store.tagline}</h2><p>{store.owner.username}, Welcome</p</li>"
    page +='<ul>'
    return page"""


def products(request):
    products =Products.objects.all()
    categories = Category.objects.all()
    context  = {'products':products, 'categories': categories}
    return render(request, 'core/products.html', context)

def product(request, id):
    product = product.objects.get(id=id)
    return render(request, 'core/detail.html', {'product':product})
    


def stores(request):
    pass
def store(request, id):
    pass
def stores_products(request, id):
    pass

def categories(request):
    pass
def category(request, id):
    pass
