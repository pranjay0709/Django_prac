from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome),
    path('signup/',views.signup),
    path('signin/',views.signin)
]
