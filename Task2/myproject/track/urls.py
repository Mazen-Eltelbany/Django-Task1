from django.urls import path
from .views import *
urlpatterns=[
    path('',alltracks),
    path('Update/<int:id>/', updatetrack ,name='updatetrack'),
    path('Insert/', inserttrack),
    path('Delete/<int:id>/', deletetrack ,name='deletetrack'),
]