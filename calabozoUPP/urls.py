"""calabozoUPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include,url
from posts.views import home_render
from django.contrib.auth.views import login,logout_then_login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include("posts.urls", namespace='list_post')),
    url(r'^post/', include("posts.urls", namespace='detalle')),
    url(r'^post/', include("posts.urls", namespace='crear_Post')),
    url(r'^home/',include("posts.urls", namespace='home')),
    url(r'^home/',include("posts.urls", namespace='about')),
    url(r'^cuentas/', include("cuentas.urls", namespace='registro')),
    url(r'^cuentas/login/', login, {'template_name':'login_form.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^home/',include("posts.urls", namespace='categorias')),
    url(r'^home/',include("posts.urls", namespace='contacto')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
