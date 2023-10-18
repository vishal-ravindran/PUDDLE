from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Category, Item
from .forms import EditItemForm, NewItemForm
from django.db.models import Q

# Create your views here.


def items(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query)
                             or Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item': item,
        'related_items': related_items,
    }

    return render(request, 'item/detail.html', context)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()

    context = {
        'form': form,
        'title': 'New Item',
    }
    return render(request, 'item/form.html', context)


@login_required
def edit(request, pk):

    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item.save()

            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    context = {
        'form': form,
        'title': 'Edit Item',
    }
    return render(request, 'item/form.html', context)


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')
