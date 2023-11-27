from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Pao

class PaoBaseView(View):
    model = Pao
    fields = '__all__'
    success_url = reverse_lazy('paes:all')

class PaoListView(PaoBaseView, ListView):
    """View to list all paes.
    Use the 'pao_list' variable in the template
    to access all Pao objects"""

class PaoDetailView(PaoBaseView, DetailView):
    """View to list the details from one pao.
    Use the 'pao' variable in the template to access
    the specific pao here and in the Views below"""

class PaoCreateView(PaoBaseView, CreateView):
    """View to create a new pao"""

class PaoUpdateView(PaoBaseView, UpdateView):
    """View to update a pao"""

class PaoDeleteView(PaoBaseView, DeleteView):
    """View to delete a pao"""


def pao_atendimento(request):
    pao_list = Pao.objects.all
    context={
        'pao_list':pao_list,
    }
    return render(request, "pao_atendimento.html", context)