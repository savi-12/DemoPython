
from django.urls import path
from . import views

app_name='ecommerceapp'


urlpatterns = [

    path('',views.allprodCat,name='allprodCat'),
    path('<slug:c_slug>/',views.allprodCat,name='Product_by_category'),
    path('<slug:c_slug>/<slug:Product_slug>/',views.proDetail,name='ProdCatdetail')
]