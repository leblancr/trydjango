from django.shortcuts import render
from .models import Product

# Product is the database
def product_detail_view(request):
    obj = Product.objects.get(id=1)  # get one of the objects from the database
    # context = {
    #     'title': obj.title,
    #     'description': obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, 'products/product_detail.html', context)