from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^blog/(?P<pk>\d+)/$', views.post_detail, name="detail"), #추가
    url(r'^post_list/$', views.post_list, name="post_list"),
    #pk: 인자
    #d+: 숫자

]