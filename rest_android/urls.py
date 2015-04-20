from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns
from simple_db import api

urlpatterns = [
    # Examples:
    # url(r'^$', 'rest_android.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/articulos/$', api.ArticuloList.as_view()),
    url(r'^api/articulos/(?P<pk>[0-9]+)/$', api.ArticuloDetail.as_view()),
    url(r'^api/pedidos/$', api.PedidoList.as_view()),
    url(r'^api/pedidos/(?P<pk>[0-9]+)/$', api.PedidoDetail.as_view()),    
]
urlpatterns = format_suffix_patterns(urlpatterns)

                  
