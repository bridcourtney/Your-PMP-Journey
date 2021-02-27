from django.shortcuts import render, redirect, \
    reverse, get_object_or_404, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    c_date = None
    if 'date_choice' in request.POST:
        c_date = request.POST['date_choice']
    bag = request.session.get('bag', {})

    if c_date:
        if item_id in list(bag.keys()):
            if c_date in bag[item_id]['items_by_c_date'].keys():
                bag[item_id]['items_by_c_date'][c_date] += quantity
                messages.success(request, f'Updated {product.name} for\
                    the {c_date.upper()} to\
                        {bag[item_id]["items_by_c_date"][c_date]} person')
            else:
                bag[item_id]['items_by_c_date'][c_date] = quantity
                messages.success(request, f'Added {product.name} for\
                     the {c_date.upper()} to your basket')
        else:
            bag[item_id] = {'items_by_c_date': {c_date: quantity}}
            messages.success(request, f'Added {product.name} for\
                 {c_date.upper()} to your basket')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to\
                 {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    c_date = None
    if 'date_choice' in request.POST:
        c_date = request.POST['date_choice']
    bag = request.session.get('bag', {})

    if c_date:
        if quantity > 0:
            bag[item_id]['items_by_c_date'][c_date] = quantity
            messages.success(request, f'Updated {product.name} for\
                 {c_date.upper()} to\
                      {bag[item_id]["items_by_c_date"][c_date]} person')
        else:
            del bag[item_id]['items_by_c_date'][c_date]
            if not bag[item_id]['items_by_c_date']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} for the\
                 {c_date.upper()}  from your basket')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to\
                 {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed\
                 {product.name} from your basket')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        c_date = None
        if 'product_c_date' in request.POST:
            c_date = request.POST['product_c_date']
        bag = request.session.get('bag', {})

        if c_date:
            del bag[item_id]['items_by_c_date'][c_date]
            if not bag[item_id]['items_by_c_date']:
                bag.pop(item_id)
            messages.success(request, f'Removed {product.name} for\
                 {c_date.upper()}  from your basket')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed\
                 {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
