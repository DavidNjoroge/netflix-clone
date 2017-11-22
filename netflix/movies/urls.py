from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^movie/',views.movie_info,name='movie_info')
]
