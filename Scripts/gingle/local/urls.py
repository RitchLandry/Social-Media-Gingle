from django.urls import path
from local.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
