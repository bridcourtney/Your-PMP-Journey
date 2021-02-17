from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('reviews/', views.all_reviews, name='reviews'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('courses/', views.courses, name='courses'),
    path('course_detail/<product_id>', views.course_detail, name='course_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
