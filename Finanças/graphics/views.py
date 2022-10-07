from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView

from django.contrib.auth import get_user_model

from .forms import GainForms, LoseForms
from .models import Gain, Lose, Financa
#Responsável pela exibiçao dos gráficos e tabelas do usuário



class GraphicPageView(TemplateView):
    template_name = 'graphics.html'

    def get_context_data(self, **kwargs):
        context = super(GraphicPageView, self).get_context_data(**kwargs)

        #Gráficos a serem utilizados
        grafico_ganhos = [['Dia/Mês', 'Valor Recebido R$']]

        grafico_pagamento = [['Dia/Mês', 'Valor Pago R$']]

        grafico_financas = [['Pagamento', 'Valor R$']]
        
        #Pegando valores do Model
        ganhos = Gain.objects.all().filter(usuario=self.request.user)
        pagamento = Lose.objects.all().filter(usuario=self.request.user)
        financa = Financa.objects.all().filter(usuario=self.request.user)

        #Organizando ganhos por data ( Todos os Ganhos )
        #.filter(data__month=10): para filtrar
        for x in ganhos.order_by('data'):
            get_allValue = [f'{x.data.day}/{x.data.month}/{x.data.year}', float(x.valor)]
            grafico_ganhos.append(get_allValue)

        #Organizando pagamento por data ( Todas os pagamentos )
        for x in pagamento.order_by('data'):
            get_allValue = [f'{x.data.day}/{x.data.month}/{x.data.year}', float(x.valor)]
            grafico_diario.append(get_allValue)

        #Pegando valores dos Financiamentos ordenado por valores
        valor_total = 0
        for x in financa.order_by('valor'):
            valor_total = (float(x.valor)/float(x.dividido)) + valor_total
            get_allValue = [x.credor, float(x.valor)/int(x.dividido), 'color: blue']
            grafico_financas.append(get_allValue)
        get_allValue = ['TOTAL', valor_total, 'color: gray']
        grafico_financas.append(get_allValue)



        


        context['ganhos'] = grafico_ganhos
        context['financas'] = grafico_financas
        context['ganhos_templateView'] = ['Ganhos', 'Data', 'chart_div']
        context['financas_templateView'] = ['Lista de Pagamentos Mensais Fixos', 'columnchart_values']

        return context


class GraphicPostView(CreateView):
    form_class = GainForms
    template_name = 'graphicsPost.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(GraphicPageView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('home')