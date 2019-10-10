from django.conf.urls import url,include
from django.contrib.auth.views import login_required

from  . import views

from .views import (
    detalle_post,
)

urlpatterns = [
    url(r'^$',views.home_render, name='home'),
    url(r'^(?P<id>\d+)/$',detalle_post,name='detalle'),
    url(r'^about',views.about_render, name='about'),
    url(r'^contacto',views.contacto_view, name='contacto'),
    url(r'^list',views.post_list, name='list_post'),
    url(r'^crear',views.crear_post ,name='crear_post'),
    url(r'^categorias',views.categoria_view, name='categ'),
    url(r'^fisico',views.cat_fisico, name='fisico'),
    url(r'^online',views.cat_online, name='online'),
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),
]
