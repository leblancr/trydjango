from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# ProductForm is a class with the database and input fields for
# the column names in the daabase. Will make a new row when submited.
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    # send the form object to the html page
    context = {
        'form': form
    }
    return render(request, 'products/product_create.html', context)

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