from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # path('', views.products_view, name='products'),
    path('', views.ProductListView.as_view(), name='products'),
    path('search/<slug:slug>/', views.category_list, name='category-list'),
    path('<slug:slug>/', views.products_detail_view, name='product-detail'),
]
