from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$',views.index,name='index'), #for pure /post url
	url(r'^details/(?P<id>\d+)/$',views.details,name='details') #
    

]