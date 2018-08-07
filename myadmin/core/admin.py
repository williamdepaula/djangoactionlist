from django.contrib import admin
from django.utils import timezone

from .models import Artigo


def publicar(modelAdmin, request, queryset):
    for artigo in queryset:
        artigo.data_publicacao = timezone.now()
        artigo.save()


class ArtigoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'texto', 'data_publicacao',]
    actions = [publicar,]

admin.site.register(Artigo, ArtigoAdmin)
