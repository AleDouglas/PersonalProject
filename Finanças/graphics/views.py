from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import GainForms, LoseForms
from .models import Gain, Lose, Financa
#Responsável pela exibiçao dos gráficos e tabelas do usuário



class GraphicPageView(LoginRequiredMixin, TemplateView):
    login_url = 'account_login'
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
        value_ganhos = 0
        for x in ganhos.filter(data__month=10).filter(data__year=2022):
            value_ganhos = value_ganhos + float(x.valor)


        #Organizando pagamento por data ( Todas os pagamentos )
        for x in pagamento.order_by('data'):
            get_allValue = [f'{x.data.day}/{x.data.month}/{x.data.year}', float(x.valor)]
            grafico_pagamento.append(get_allValue)

        value_pagamentos = 0
        for x in pagamento.filter(data__month=10).filter(data__year=2022):
            value_pagamentos = value_pagamentos + float(x.valor)

        #Pegando valores dos Financiamentos ordenado por valores
        valor_mensal_financa = 0
        valor_total_financa = 0
        for x in financa.order_by('valor'):
            valor_total_financa = float(x.valor) + valor_total_financa
            valor_mensal_financa = (float(x.valor)/int(x.dividido)) + valor_mensal_financa
            get_allValue = [x.credor, float(x.valor)/int(x.dividido), 'color: blue']
            grafico_financas.append(get_allValue)
        get_allValue = ['TOTAL', valor_mensal_financa, 'color: gray']
        grafico_financas.append(get_allValue)



        
        #GERANDO DADOS DOS GRÁFICOS
        context['ganhos'] = grafico_ganhos
        context['financas'] = grafico_financas
        context['ganhos_templateView'] = ['Ganhos', 'Data', 'chart_div']
        context['financas_templateView'] = ['Lista de Pagamentos Mensais Fixos', 'columnchart_values']

        #GERANDO DADOS DO RELATÓRIO
        context['relatorio_mensais'] = financa.order_by('inicio').order_by('credor')
        context['divida_total'] = valor_total_financa
        context['divida_mensal'] = valor_mensal_financa
        context['pagamento_mes'] = value_pagamentos
        context['ganhos_mes'] = value_ganhos
        context['saldo_apos'] = value_ganhos - value_pagamentos
        return context


class GraphicPostView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    form_class = GainForms
    template_name = 'postGain.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(GraphicPageView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('GraphicPage')

class GraphicPostLoseView(LoginRequiredMixin, CreateView):
    login_url = 'account_login'
    form_class = LoseForms
    template_name = 'postLose.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.usuario = self.request.user
        self.object.save()
        return super(GraphicPostLoseView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('GraphicPage')