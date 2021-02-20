from django import forms
from .widgets import CustomClearableFileInput
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial

        fields = ('content', 'image',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)
   