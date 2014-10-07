from django.conf.urls import patterns, url
from file import views
from file.views import File,ImageView,RatingView

urlpatterns = patterns('',
	url(r'^$',File.as_view(), name='index'),
	url(r'^image/(?P<action>[a-z]+)/(?P<imageId>[a-zA-Z0-9-]+)/$', ImageView.as_view(), name='image'),
	url(r'^image/(?P<action>[a-z]+)/$', ImageView.as_view(), name='image'),
	url(r'^image/$', ImageView.as_view(), name='image'),
	url(r'^rating/', RatingView.as_view(), name='rating')
	# url(r'^list/image/', ImageList.as_view(), name='imagelist'),
	# url(r'^detail/image/(?', ImageDetail.as_view(), name='imageDetail')
	# url(r'^upload/', views.upload, name="upload"),
	# url(r'^list/', views.list, name="list"),
 #    url(r'^getImage/(?P<imageId>[a-zA-Z0-9-]+)/$', views.getImage, name="getImage"),
 #    url(r'^showImage/(?P<imageId>[a-zA-Z0-9-]+)/$', views.showImage, name="showImage"),
 #    url(r'^submitRating/', views.submitRating, name="submitRating")
)
