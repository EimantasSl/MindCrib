from django.conf.urls import url

from . import views

app_name = 'entries'

urlpatterns = [
    url(r'^$', views.HomeListView.as_view(), name='home'),
]