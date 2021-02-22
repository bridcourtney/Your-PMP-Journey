from django.db import models
from django.contrib.auth.models import User


# Models
class Testimonial(models.Model):
    """Model to give our Course atendants an
    opportunity to say how good our course was"""
    full_name = models.CharField(max_length=70, null=True, blank=True)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content