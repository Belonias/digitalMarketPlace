from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
from .forms import ProductForm, ProductModelForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from digitalmarket.mixins import MultiSlugMixin
# Create your views here.

class ProductListView(ListView):
    model = Product

class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product

    # def get_object(self, *args, **kwargs):
    #     print(self.kwargs)  # related to request
    #     ModelClass = self.model
    #     slug = self.kwargs.get('slug')
    #     if slug is not None:
    #         try:
    #             obj = get_object_or_404(ModelClass, slug=slug)
    #         except ModelClass.MultipleObjectsReturned:
    #             obj = ModelClass.objects.filter(slug=slug).order_by('-sale_price').first()
    #     else:
    #         obj = super(ProductDetailView, self).get_object(*args, **kwargs)
    #     return obj

class ProductCreateView(CreateView):
    pass

def update_view(request, object_id=None):
    product = get_object_or_404(Product, id=object_id)
    form = ProductModelForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save(commit=False)
        form.save()
    context = {
        'object': product,
        'form': form,
    }
    # edit for update view
    template = 'products/update_view.html'
    return render(request, template, context)

def create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        instance = form.save(commit=False)
        form.save()
    template = 'products/create_view.html'
    context = {
        # 'object': product,
        'form': form,
    }
    return render(request, template, context)

def detail_slug_view(request, slug=None):
    if slug is not None:
        try:
            product = get_object_or_404(Product, slug=slug)
        except Product.MultipleObjectsReturned:
            product = Product.objects.filter(slug=slug).order_by('-title').first()
        # product = Product.objects.get(id=object_id)
        template = 'products/product_detail_view.html'
        context = {
            "object": product,
        }
        return render(request, template, context)
    else:
        raise Http404

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
