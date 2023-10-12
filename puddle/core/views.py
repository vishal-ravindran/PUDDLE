from django.shortcuts import redirect, render
from item.models import Category, Item
from .forms import SignupForm


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold = False)
    categories = Category.objects.all()
    context ={
        'items': items,
        'categories' : categories,
    }
    return render(request, 'core/index.html', context=context)

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect ('/login/')

    else:
        form = SignupForm()

    context = {
        'form' : form,
    }

    return render(request, 'core/signup.html', context)