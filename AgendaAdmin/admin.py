from datetime import timedelta

from django.contrib import admin
from django.utils.timezone import now

from AgendaAdmin.models import ItemAgenda,LocalEvento
from django.conf.locale.pt_BR import formats as pt_BR_formats


admin.site.site_header='Painel de Controle'
admin.site.site_title='Agenda'
admin.site.index_title='Recursos'


admin.site.register(ItemAgenda)
admin.site.register(LocalEvento)

class ItemAgendaAdmin(admin.ModelAdmin):
    list_display = (
        'data','hora','titulo',
        'criado_em','criado_recente'
    )
    date_hierarchy = 'data'
    search_fields = ('titulo',)
    filter_horizontal = ('participantes',)

    list_filter = ('criado_em',)

    def criado_recente(self,obj):
        return obj.criado_em >= now() - timedelta(minutes = 30)

    criado_recente.short_description = 'recente?'
    criado_recente.boolean = True


    def data(sel,obj):
    	return obj.data.strftime('%d/%m/%Y')

    data.short_description = 'data'


    class Meta:

    	ordering = ('-data','hora')