from django.conf.urls import url
from paste_wall import views

urlpatterns = [
    url(r'^add/$', views.PasteCreateView.as_view(), name='paste_wall-add'),
    url(r'^(?P<pk>[0-9]+)/pass/$', views.PassCheckView.as_view(), name='paste_wall-pass'),
    url(r'^unchecked/list/$', views.UncheckedPasteView.as_view(), name='paste_wall-unchecked-list'),
    url(r'^all/list/$', views.PasteListView.as_view(), name='paste_wall-list'),
    url(r'^timeline/$', views.PasteTimeLineView.as_view(), name='paste_wall-time-line'),
    url(r'^success/$', views.PasteSuccessView.as_view(), name='paste-success')
]
