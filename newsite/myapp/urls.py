from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^hello/$', view=views.hello, kwargs={'age': 23, }, name='hello'),
    url(r'^(?P<name>\w+)/(?P<age>\d+)/', view=views.info, name='info')
]
