from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
  
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    HARDBACK = 'Hardback'
    KINDLE = 'Kindle'
    PAPERBACK = 'Paperback'
    NONE = 'None'
    BOOK_TYPE_CHOICES = [
        (HARDBACK, 'Hardback'),
        (KINDLE, 'Kindle'),
        (PAPERBACK, 'Paperback'),
        ('', '')
    ]
    book_type = models.CharField(max_length=254, choices=BOOK_TYPE_CHOICES, blank=True, default='')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.TextField()
    is_a_service = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True,
                                   validators=[MinValueValidator(1),
                                               MaxValueValidator(100)])
   

    def __str__(self):
        return self.name