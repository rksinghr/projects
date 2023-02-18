from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profile, name='profile'),
    path('signout', views.signout, name='signout'),
    path('add_event', views.add_event, name='add_event'),
    path('mytime', views.usrdta, name='mytime'),
    path('perdata', views.perdta, name='perdata'),
    path('testsel', views.select_test, name='testsel'),    
]