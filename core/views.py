from django.views.generic import TemplateView

from .models import Servico, Funcionario

class IndexView(TemplateView):
    template_name = 'index.html'


