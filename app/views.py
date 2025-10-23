from django.shortcuts import render
from .models import Product, Brand, Category

# Create your views here.
def index(request):

    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Brand.objects.all()

    context = {
        "products": products,
        "brands" : brands,
        "categories" : categories,
    }

    return render(request, "app/index.html")