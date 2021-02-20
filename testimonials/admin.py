from django.contrib import admin
from .models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'content',
        'created',
        'image',
        'full_name',
    )

    ordering = ('user',)


admin.site.register(Testimonial, TestimonialAdmin)
