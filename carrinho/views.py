from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Carrinho
from paes.models import Pao

def adiciona_carrinho(request, pao_id):
    pao = Pao.objects.filter(id=pao_id).first()

    item = Carrinho.objects.filter(pao=pao).first()

    if item:
        item.quantidade += 1
        item.save()
        messages.success(request, "Item adicionado ao carrinho!")
    else:
        Carrinho.objects.create(pao=pao)
        messages.success(request, "Item adicionado ao carrinho!")

    return redirect("carrinho:detalha_carrinho")

def remove_carrinho(request, id):
    item = get_object_or_404(Carrinho, id=id)

    item.delete()
    messages.success(request, "Item removido do carrinho!")

    return redirect("carrinho:detalha_carrinho")

def detalha_carrinho(request):
    itens = Carrinho.objects.all()
    valor_total = sum(item.quantidade * item.pao.valor for item in itens)

    context = {
        "itens": itens,
        "valor_total": valor_total,
    }

    return render(request, "carrinho/detalha_carrinho.html", context)


def finaliza_pedido(request):
    Carrinho.objects.all().delete()
    messages.success(request, "Pedido finalizado!")

    return redirect("paes:pao_atendimento")