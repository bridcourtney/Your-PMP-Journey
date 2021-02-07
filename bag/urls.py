from django.conf.urls import url
from .views import view_bag, add_to_bag, adjust_bag

urlpatterns = [
    url(r'^$', view_bag, name='view_bag'),
    url(r'^add/(?P<id>\d+)', add_to_bag, name='add_to_bag'),
    url(r'^adjust/(?P<id>\d+)', adjust_bag, name='adjust_bag'),
]