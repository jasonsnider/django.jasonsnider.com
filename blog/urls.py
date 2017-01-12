from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<slug>[\w\-]+)/$', views.DetailView.as_view(), name='detail')  # New!
]
