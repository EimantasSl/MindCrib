from django.conf.urls import url

from . import views

app_name = 'users'

urlpatterns = [
    url(r'^profile/$', views.ProfileDetailView.as_view(), name='my-profile'),
    url(r'^profile/update/$', views.ProfileUpdateView.as_view(), name='profile-update'),
    url(r'^profile/(?P<username>\w+)$', views.ProfileDetailView.as_view(), name='profile'),
]