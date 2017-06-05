from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
# Create your views here.
def detail_view(request, object_id=None):
    if object_id is not None:
        product = get_object_or_404(Product, id=object_id)
        # product = Product.objects.get(id=object_id)
        template = 'products/product_detail_view.html'
        context = {
            "object": product,
        }
        return render(request, template, context)
    else:
        raise Http404


def list_view(request):
    queryset = Product.objects.all()
    context = {
        'product_list': queryset,
    }
    template = 'products/product_list_view.html'
    return render(request, template, context)
