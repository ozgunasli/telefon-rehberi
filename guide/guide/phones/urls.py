from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.NumberListView.as_view(), name='number_list'),
    url(r'^(?P<pk>\d+)$', views.number_detail, name='number_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$',
        views.NumberUpdateView.as_view(),
        name='number_update'),
    url(r'^delete/(?P<pk>[0-9]+)/$',
        views.NumberDeleteView.as_view(),
        name='number_delete'),
    url(r'^create/$', views.NumberCreateView.as_view(), name='number_create'),
    url(r'^group/$', views.GroupListView.as_view(), name='group_list'),
    url(r'^group/(?P<pk>\d+)$', views.group_detail, name='group_detail'),
    url(r'^group/(?P<pk>[0-9]+)/update/$',
        views.GroupUpdateView.as_view(),
        name='group_update'),
    url(r'^group/delete/(?P<pk>[0-9]+)/$',
        views.GroupDeleteView.as_view(),
        name='group_delete'),
    url(r'^group/create/$',
        views.GroupCreateView.as_view(),
        name='group_create'),
]