from django.urls import path
from . import views

urlpatterns=[
    path('car',views.car),
    path('bike',views.bike)
]