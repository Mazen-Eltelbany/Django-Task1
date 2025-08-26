from django.urls import path
from .views import *
urlpatterns=[
    path('',alltracks,name='alltracks'),
    path('Update/<int:id>/', updatetrack ,name='updatetrack'),
    path('Insert/', inserttrack,name='inserttrack'),
    path('Delete/<int:id>', deletetrack ,name='deletetrack'),
]