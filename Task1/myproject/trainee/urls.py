from django.urls import path
from .views import *
urlpatterns = [
    path('', alltraunees),
    path('add/', addtrainee),
    path('update/<int:id>/', updatetrainee ,name='update'),
    path('delete/<int:id>/', deletetrainee,name='delete'),
    path('gettrainee/<int:id>/', gettraineebyid,name='getbyid'),
]