from django.conf.urls import url
from statistics import views

urlpatterns = [
    url(r'^add/$', views.InfoCreateView.as_view(), name='info-add'),
    url(r'^list/$', views.InfoListView.as_view(), name='info-list'),
    url(r'^success/$', views.SignupSuccessView.as_view(), name='signup-success'),
    url(r'^gen_csv/$', views.GenCSVView.as_view(), name='info-output')
]
