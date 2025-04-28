# TODO: Configure as URLs para a API.
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import ItemPMVGViewSet, StatsAPIView # Descomente quando as views existirem

# Exemplo usando DefaultRouter para ViewSets:
# router = DefaultRouter()
# router.register(r'items', ItemPMVGViewSet, basename='itempmvg')

urlpatterns = [
    # path('', include(router.urls)), # Descomente para usar o router
    # path('stats/', StatsAPIView.as_view(), name='item-stats'), # Exemplo de URL para view de stats
    path('ping/', lambda request: HttpResponse("pong"), name="ping"), # URL simples para teste
]

# Adicione um import HttpResponse se usar o lambda acima
from django.http import HttpResponse
