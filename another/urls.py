from django.urls import path

from another import views

urlpatterns = [
    path('data/', views.data, name='data')
]
