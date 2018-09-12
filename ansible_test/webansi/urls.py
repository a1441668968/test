from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', view=views.index, name='index'),
    url(r'^addhosts/$', view=views.addhosts, name='addhosts'),
    url(r'^addmodules/$', view=views.addmodules, name='addmodules'),
    url(r'^tasks/$', view=views.tasks, name='tasks'),
]
