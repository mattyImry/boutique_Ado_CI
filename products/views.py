from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ show all product, including sorting and search query """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
