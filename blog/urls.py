from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^globalbuster/$', views.globalbuster, name='globalbuster'),
    url(r'^globalbusteractive/$', views.globalbusteractive, name='globalbusteractive'),
    url(r'^login/$', views.login, name='login'),
]
