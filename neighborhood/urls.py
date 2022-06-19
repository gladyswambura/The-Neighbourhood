from django.urls import path, include
from . import views
from .views import *
from . import views as app_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # MAIN PAGE                                      
    path('', views.index, name='index'),

    # PROFILE SECTION
    path('profile/', views.profile, name='users-profile'),
    

    #HOOD SECTION
    path('all-hoods/', views.hoods, name='hood'),
    path('new-hood/', views.create_hood, name='new-hood'),

]