from django.contrib import admin
from .models import Linguagem, Curso, Vaga
# Register your models here.



class LiguagemAdmin(admin.ModelAdmin):
	fieldsets = [(
		'Informacoes da Linguagem', {'fields':[ 'lingua','descLingua']},
	)]



admin.site.register(Linguagem, LiguagemAdmin)
admin.site.register(Curso )
admin.site.register(Vaga)