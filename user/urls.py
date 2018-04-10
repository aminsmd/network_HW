from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^login/$',views.login,name="login"),
    url(r'^logiin/(?P<un>[\w\-]+)/(?P<pw>[\w\-]+)',views.logiin,name="login"),
    #url(r'^withdraw/',)

]