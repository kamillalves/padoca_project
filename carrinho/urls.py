from django.urls import path
from . import views

app_name = "carrinho"

urlpatterns = [
    path("adiciona_carrinho/<int:pao_id>/", views.adiciona_carrinho, name="adiciona_carrinho"),
    path("remove_carrinho/<int:id>/", views.remove_carrinho, name="remove_carrinho"),
    path("detalha_carrinho", views.detalha_carrinho, name="detalha_carrinho"),
    path("finaliza_pedido", views.finaliza_pedido, name="finaliza_pedido"),

]