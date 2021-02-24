from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, id):

    # Add a quantity of the specified product to the bag
    
    product = get_object_or_404(Product, pk=id)
    
    try:
        quantity = int(request.POST.get('quantity'))
    except:
        quantity = 1


    bag = request.session.get('bag', {})
    if id in bag:
        bag[id] = int(bag[id]) + quantity
    else:
        bag[id] = bag.get(id, quantity)
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(reverse('products'))


def adjust_bag(request, id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=id)

        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[id]}')
        else:
            bag.pop(id)
            messages.success(request, f'Removed {product.name} from your bag')
            
        request.session['bag'] = bag
        return redirect(reverse('view_bag'))

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)