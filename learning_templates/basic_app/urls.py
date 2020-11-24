from django.urls import path
from basic_app import views

#Template tagging. Set a global variable name that django will auto look for.


urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
