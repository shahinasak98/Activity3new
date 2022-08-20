from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.create),
    path('go',views.conversion),
    path('index.html',views.back)
]
