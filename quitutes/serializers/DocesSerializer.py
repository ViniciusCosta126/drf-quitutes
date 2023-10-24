from rest_framework import serializers
from quitutes.models import Doce

class DocesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doce
        fields = ['id','nome','peso','descricao','valor','image','categoria']