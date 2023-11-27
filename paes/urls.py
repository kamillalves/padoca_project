
from django.urls import path
from . import views

app_name = 'paes'

urlpatterns = [
    path('', views.PaoListView.as_view(), name='all'),
    path('paes/<int:pk>/detail', views.PaoDetailView.as_view(), name='pao_detail'),
    path('paes/create/', views.PaoCreateView.as_view(), name='pao_create'),
    path('paes/<int:pk>/update/', views.PaoUpdateView.as_view(), name='pao_update'),
    path('paes/<int:pk>/delete/', views.PaoDeleteView.as_view(), name='pao_delete'),
    path('paes/atendimento', views.pao_atendimento, name='pao_atendimento'),

]