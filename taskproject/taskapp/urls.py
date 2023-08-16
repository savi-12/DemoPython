from. import views
from django.urls import path





urlpatterns = [

    # path('',views.demo,name='demo'),
    #  path('about/',views.about,name="about"),
    # path('contact/',views.contact,name="contact"),
    # path('detail/',views.detail,name="detail"),
    # path('thanks/',views.thanks,name="Thank you")
    path('', views.demo, name='demo'),
    # path('add/',views.result,name='result')
]
