from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^new/profile$', views.add_profile, name='edit'),
    url(r'^myprofile$',views.my_profile,name ='myprofile'),