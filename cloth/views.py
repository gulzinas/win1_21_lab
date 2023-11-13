# cloth/views.py
from django.shortcuts import render, redirect
from .models import Product, Tag
from .forms import OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def tag_filtered_list(request, tag_id):
    tag = Tag.objects.get(pk=tag_id)
    products = Product.objects.filter(tags=tag)
    return render(request, 'tag_filtered_list.html', {'products': products, 'tag': tag})

def all_tags(request):
    tags = Tag.objects.all()
    return render(request, 'all_tags.html', {'tags': tags})

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html')
