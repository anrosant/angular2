from django.conf.urls import url
from pruebaApp import views


urlpatterns = [
    url(r'^pruebaApp/$', views.platillo_list),
    url(r'^pruebaApp/(?P<idP>[0-9]+)/$', views.platillo_detail),
]
