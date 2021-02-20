from django.contrib import admin
from .models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'content',
        'created',
        'image',
    )

    ordering = ('title',)


admin.site.register(Testimonial, TestimonialAdmin)
