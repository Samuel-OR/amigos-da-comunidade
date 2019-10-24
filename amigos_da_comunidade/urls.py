from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edicao/', include('amigos_da_comunidade.edicao.urls', namespace='edicao')),
    path('', include('amigos_da_comunidade.website.urls', namespace='website')),
    path('atendimento/', include('amigos_da_comunidade.atendimento.urls', namespace='atendimento')),
    path('core/', include('amigos_da_comunidade.core.urls', namespace='core')),
    path('accounts/', include('amigos_da_comunidade.accounts.urls', namespace='accounts')),

]
