from django.shortcuts import render
from .models import Product
# Create your views here.
def detail_view(request):
#    query = Product.objects.get(id=pk)
    context = {
        #"product": query
    }
    template = 'products/product_detail_view.html'
    return render(request, template, context)

def list_view(request):
    queryset = Product.objects.all()
    context = {
        'product_list': queryset,
    }
    template = 'products/product_list_view.html'
    return render(request, template, context)
