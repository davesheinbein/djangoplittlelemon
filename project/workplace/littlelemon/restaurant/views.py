from django.shortcuts import render
from .forms import BookingForm
from .models import MenuItem

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'book.html', context)


def menu(request):
    if MenuItem.objects.exists():
        menu_items = MenuItem.objects.all().order_by('name')  # Alphabetical order
    else:
        menu_items = []  

    return render(request, 'menu.html', {'menu_items': menu_items})


def menu_item_detail(request, id):
    if MenuItem.objects.exists():
        menu_item = MenuItem.objects.get(pk=id)
        print("menu_item", menu_item)
    else:
        menu_items = []
    return render(request, 'menu_item.html', {'menu_item': menu_item})
