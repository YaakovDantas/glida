from django.conf import settings
from home.models import Gerente, Contato, Artigo, Tema
import re, datetime
EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'URLS_PERSONAL_MIDDLEWARE'):
    EXEMPT_URLS += [re.compile(url) for url in settings.URLS_PERSONAL_MIDDLEWARE]

class DataDashboard(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info.lstrip('/')
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        dia_atual = datetime.date.today()
        if url_is_exempt:
            
            
            try:
                user = request.user if request.user.is_active  else False
                gerente = user.gerente
                mensagens_nao_lidas = Contato.objects.filter(lido=False)
                artigos_nao_lidos = Artigo.objects.filter(ativo=False)
                request.dia_atual = dia_atual
                request.user_logado = user
                request.gerente = gerente
                request.mensagens_nao_lidas = mensagens_nao_lidas
                request.artigos_nao_lidos = artigos_nao_lidos
            except:
                pass

        else:
            temas = Tema.objects.all()
            request.temas = temas
            try:    
                user = request.user.usuario if request.user.is_active  else False
                request.user_logado = user
            except:
                pass


        return None
