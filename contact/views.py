from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from .forms import ContactUsForm
from profiles.models import UserProfile


def contact(request):
    """
    This view will return the Contact Us template and render the form
    """
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            user_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    # The user email will be captured and
                    # displayed in the subject field
                    f"Message from {full_name}, <{user_email}>",
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_success_message')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        # get logged in user full_name and email from profile model
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            user_email = profile.user.email
            form = ContactUsForm(initial={
                'full_name': profile.default_full_name,
                'email': user_email,
                })
        else:
            form = ContactUsForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success_message(request):
    """
    This view will confirm to the user that
    the email was sent successfully to website
    """
    return render(request, 'contact/contact_success_message.html')
