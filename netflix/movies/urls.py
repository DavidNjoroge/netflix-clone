from django.conf.urls import url
from . import views




urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^ke/$',views.landing_page,name='landing_page'),
]