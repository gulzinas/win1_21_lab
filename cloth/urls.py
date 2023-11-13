# cloth/urls.py
from django.urls import path
from .views import product_list, tag_filtered_list, all_tags, create_order
from .views import success_page

urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('tags/<int:tag_id>/', tag_filtered_list, name='tag_filtered_list'),
    path('all_tags/', all_tags, name='all_tags'),
    path('create_order/', create_order, name='create_order'),
    path('success/', success_page, name='success_page'),

]
