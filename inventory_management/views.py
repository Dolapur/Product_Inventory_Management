from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.contrib import messages
from django.utils import timezone


def product_display(request):
    products = Product.objects.all()
    return render(request, 'product_display.html', {"products": products})


def product_creation(request):
    form = ProductForm()
    if request.method == "POST":
       form = ProductForm(request.POST)
       if form.is_valid():
            form.save()
            return redirect('product_display')
    return render(request, 'product_form.html', {'form': form})


def product_update(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.date_created = timezone.now().date()
            product.time_created = timezone.now().time()
            product.save()
            messages.success(request, 'Product updated successfully.', extra_tags='success')
            return redirect('product_display')
    return render(request, 'product_form.html', {'form': form})


def product_delete(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully.', extra_tags='success')
        return redirect('product_display')
    return render(request, 'product_del.html', {'product': product})


