from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^postlist$', views.post_list, name='post_list'),
    url(r'^$', views.globalbuster, name='globalbuster'),
    url(r'^globalbusteractive/$', views.globalbusteractive, name='globalbusteractive'),
    url(r'^login/$', views.login, name='login'),
]
