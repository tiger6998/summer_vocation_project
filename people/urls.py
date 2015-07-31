from django.conf.urls import patterns, url
from people import views

urlpatterns = patterns('',
	url(r'^add_people/$', views.add_people, name='add_people'),
	url(r'^detail/(?P<people_name_slug>[\w\-]+)/$', views.people, name='people'),
	)