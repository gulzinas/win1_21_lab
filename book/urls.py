from django.urls import path
from . import views


urlpatterns = [
    path('book', views.book_view),
    path('lang_detail/<int:id>/', views.book_detail_view),
    path('add-cooment/', views.createBookView),
]
