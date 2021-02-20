import os
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from profiles.models import UserProfile
from .models import Testimonial
from django.contrib.auth.models import User


def testimonials(request):
    """ A view to show all testimonial """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/includes/testimonials.html', context)



@login_required
def add_testimonial(request):
    """
    This view will return the Testimonial template and render the form
    """
    if request.method == 'POST':
        # Get values from form
        profile = UserProfile.objects.get(user=request.user)
        form = Testimonial(
            content=request.POST.get('content'),
            image=request.POST.get('image'),
            full_name = profile.default_full_name,
            user=request.user
        )

        form.save()
        messages.success(request, 'Thank you for submitting your Testimonial')
        return redirect('products')

    context = {
        'form': TestimonialForm
    }
    return render(request, 'testimonials/add_testimonial.html', context)