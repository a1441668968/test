from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^hello/$', view=views.hello, kwargs={'age': 23, }, name='hello'),
    url(r'^(?P<name>\w+)/(?P<age>\d+)/', view=views.info, name='info'),
    url(r'^home/$', view=views.home, name='home'),
    url(r'^protect/$', view=views.protect, name='protect'),
    url(r'^login/$', view=views.login, name='login'),
    url(r'^template/$', views.template, name='template'),
]
