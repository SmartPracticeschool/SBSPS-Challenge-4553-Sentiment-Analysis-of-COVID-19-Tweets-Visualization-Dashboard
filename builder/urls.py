from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('blank/', views.blank),
    path('contact/', views.contact),
    path('crowd_pred/', views.crowd_pred),
    path('crowd_prediction/', views.crowd_prediction),
    path('fake_info/', views.fake_info),
    path('fake_info_prediction/', views.fake_info_prediction),
    path('general/', views.general),
    path('location_analysis/', views.location_analysis),
    path('login/', views.login),
    path('profile/', views.profile),
    path('thank_you/', views.thank_you),
    path('widgets/', views.widgets),

]