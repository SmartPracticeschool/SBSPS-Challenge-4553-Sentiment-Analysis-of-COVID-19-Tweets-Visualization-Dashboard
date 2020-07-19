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
    path('fake_info_result/', views.fake_info_result),
    path('general/', views.general),
    path('location_analysis/', views.location_analysis),
    path('location_analysis_report/', views.location_analysis_report),
    path('login/', views.login),
    path('profile/', views.profile),
    path('thank_you/', views.thank_you),
    path('thank_you_fakeinfo/', views.thank_you_fakeinfo),
    path('widgets/', views.widgets),

]