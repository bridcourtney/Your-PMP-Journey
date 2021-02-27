from django.shortcuts import render
from products.models import ProductReview, DatesAvailable
from testimonials.models import Testimonial
# Create your views here.


def index(request):
    """ A view to return the Product Reviews,
    Testimonials & Course Dates to the index
    page
    """

    reviews = ProductReview.objects.all()
    testimonials = Testimonial.objects.all()
    dates = DatesAvailable.objects.all()

    context = {
        'reviews': reviews,
        'testimonials': testimonials,
        'dates': dates,
    }

    return render(request, 'home/index.html', context)