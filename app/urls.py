from django.urls import path
from app import views

urlputterns=[
  path('',views.IndexView.as_view(),name='index'),
]