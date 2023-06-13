from rest_framework import serializers
from historico.api.serializers import HistoricosDetalhesSerializer
from agendamentos.models import Agendamentos

class AgendamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamentos
        fields = '__all__'


class AgendamentosDetalhesSerializer(serializers.ModelSerializer):
    historicos = HistoricosDetalhesSerializer(many=True,read_only=True)

    class Meta:
        model = Agendamentos
        fields = [
            'id_agendamento',
            'data_hora',
            'data_criacao',
            'cancelado',
            'obs',
            'tipo',
            'id_paciente',
            'historicos'
        ]