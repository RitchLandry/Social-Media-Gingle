from django.urls import path
from local.views import Index,registerUser,logout

urlpatterns = [
    path('', Index, name='index'),
    path('logout',logout,name="logout"),
    path('register',registerUser,name="register")
]
