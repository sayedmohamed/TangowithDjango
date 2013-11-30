from django.conf.urls import url,patterns,include
from rango import views

urlpatterns=patterns('',
                     url(r'^$',views.index,name='index'),
                     url(r'^about/$',views.about,name='about'),
                     )
