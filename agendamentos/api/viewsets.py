from rest_framework import viewsets
from agendamentos.api.serializers import AgendamentosSerializer
from agendamentos.models import Agendamentos

class AgendamentosViewSet(viewsets.ModelViewSet):
    queryset = Agendamentos.objects.all().order_by('data_hora')
    serializer_class = AgendamentosSerializer