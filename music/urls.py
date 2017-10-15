from django.conf.urls import url
from . import views

app_name = 'music'
urlpatterns = [
	#/music/
	url(r'^$', views.index, name='index'),

	#/music/21--example
	#we use () to treat 21 as one number and not 2 and 1 individually
	# ?P<album_id> is the way by which we save the album id as a variable
	# hence 21 will be saved as album_id
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

	#for writing the favorite logic
	url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]