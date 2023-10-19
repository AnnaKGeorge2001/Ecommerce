from django.urls import path

from ecommerce_app import views
app_name='ecommerce_app'
urlpatterns = [
    path('',views.allProductCategory,name='allProductCategory'),
    path('<slug:c_slug>/',views.allProductCategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.prodDetail, name='prodCatdetail'),

]