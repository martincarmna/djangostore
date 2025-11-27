from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from .forms import CategoryForm


def index(request):
    return render(request, 'products/index.html')


def category_list(request):
    categories = Category.objects.all()
    return render(
        request,
        'products/category_list.html',
        {"categories": categories}
    )


def category_new(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')

    return render(
        request,
        'products/category_new.html',
        {"form": form}
    )


def category_detail(request, cat_id):

    category = get_object_or_404(Category, id=cat_id)

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')

    return render(
        request,
        'products/category_detail.html',
        {"category": category, "form": form}
    )


def category_update(request, cat_id):

    category = get_object_or_404(Category, id=cat_id)

    form = CategoryForm(instance=category)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')

    return render(
        request,
        'products/category_update.html',
        {"category": category, "form": form}
    )


def category_delete(request, cat_id):

    category = get_object_or_404(Category, id=cat_id)

    if request.method == 'POST':
        category.delete()
        return redirect('products:category_list')

    return render(
        request,
        'products/category_delete.html',
        {"category": category}
    )
