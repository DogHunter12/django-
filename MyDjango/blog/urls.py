from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='h-home'),
    url(r'^about$', views.about, name='h-about'),
    url(r'^movies/(?P<movie_id>\d+)[/]?$', views.movies, name='h-movies'),
]
