from django.conf.urls import url

from core.views import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', main_page, name="main_page"),
    url(r'^registration/$', RegistrationFormView.as_view(), name="registration_page"),
    url(r'^users_list/$', users_list_page, name="users_list_page"),
    url(r'^profile/(?P<name_of_user>\w+)/$', profile_page, name="profile_page"),
    url(r'^home/$', home_page, name="home_page"),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name="login_page"),
    url(r'^logout/$', logout, {'template_name': 'core/logout.html'}, name="logout_page"),
]