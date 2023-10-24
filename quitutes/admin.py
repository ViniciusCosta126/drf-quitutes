from django.contrib import admin
from quitutes.models import Doce


class DoceAdmin(admin.ModelAdmin):
    list_display = ('nome','valor','peso','categoria','ativo')


admin.site.register(Doce,DoceAdmin)