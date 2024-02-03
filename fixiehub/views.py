from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'pages/home.html', {'items': items})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'pages/item-list.html', {'items': items})

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    return render(request, 'pages/item-create.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('edit_item', item_id=item_id) 
    else:
        form = ItemForm(instance=item)

    return render(request, 'pages/item-edit.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    return redirect('item_list')
