from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^backgd$', views.backgd, name='backgd'),
    url(r'^projs',views.projs,name='projs'),
    url(r'^contact$',views.contact,name='contact'),
]