from django.db import models
from django.contrib.auth.models import User


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
    is_a_video = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        """
        this fuction caculates the average customer rating
        """
        self.total = sum(int(review['stars']) for review in self.reviews.values())
        if self.total > 0:
            return round(self.total / self.reviews.count(), 1)
        else:
            return self.total


class ProductReview(models.Model):
    content = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', related_query_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews', related_query_name='reviews')
    stars = models.IntegerField(null=False, blank=False, default=0)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.content


class DatesAvailable(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='available', related_query_name='available')
    date_available = models.CharField(max_length=254, null=True, blank=True)


    def __str__(self):
        return self.date_available
