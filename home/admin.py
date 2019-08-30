from django.contrib import admin
from .models import Gerente, Redator, Artigo, Comentario, Visualizacao, Tema, Acesso, Contato, Sugestao
# Register your models here.

class GerenteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'ativo', )

class RedatorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'email', 'ativo', )

class ComentarioInline(admin.TabularInline):
	model = Comentario
	extra = 0

class ArtigoAdmin(admin.ModelAdmin):
	list_display = ('redator', 'titulo', 'ativo', )
	inlines = [ComentarioInline]
	class Meta:
		model = Artigo 

class ComentarioAdmin(admin.ModelAdmin):
	list_display = ('artigo', 'leitor', 'ativo', )

class TemaAdmin(admin.ModelAdmin):
	list_display = ('nome', )

class VisualizacaoAdmin(admin.ModelAdmin):
	list_display = ('nome','data', )

class AcessoAdmin(admin.ModelAdmin):
	list_display = ('data', )

class ContatoAdmin(admin.ModelAdmin):
	list_display = ('nome','assunto' )

class SugestaoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'assunto','visto', )








admin.site.register(Gerente, GerenteAdmin)
admin.site.register(Redator, RedatorAdmin)
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Visualizacao, VisualizacaoAdmin)
admin.site.register(Acesso, AcessoAdmin)
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Sugestao, SugestaoAdmin)
