from django.conf.urls import url
from . import views

urlpatterns = [
    # url patterns to display in the browser
    url(r'^$', views.home, name='home'),
    url(r'^details/(?P<slug>[.\-\w]+)/$', views.details, name='details'),
    url(r'^add/movies/$', views.add_movies, name='add_movies'),
    url(r'^update/movies/(?P<slug>[.\-\w]+)/$', views.update_movie, name='update_movie'),
    url(r'^delete/(?P<slug>[.\-\w]+)/$', views.delete_movie, name='delete_movie'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^add-review/(?P<slug>[.\-\w]+)/$', views.add_review, name='add_review'),
    url(r'^edit-review/(?P<slug>[.\-\w]+)/(?P<id>[\d]+)/$', views.edit_review, name='edit_review'),
    url(r'^delete-review/(?P<slug>[.\-\w]+)/(?P<id>[\d]+)/$', views.delete_review, name='delete_review'),
    url(r'^profile/(?P<user>[.\-\w]+)/$', views.profile, name='profile')
]