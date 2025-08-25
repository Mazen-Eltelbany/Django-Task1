from django.urls import path
from .views import *
urlpatterns = [
    path('', alltraunees,name='alltrainees'),
    path('insert/', inserttrainee ,name='insert'),
    path('update/<int:id>/', updatetrainee ,name='update'),
    path('delete/<int:id>/', deletetrainee,name='delete'),
    path('gettrainee/<int:id>/', gettraineebyid,name='getbyid'),
]