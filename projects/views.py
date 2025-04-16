from rest_framework import viewsets
from .models import Project, Agent, FloorPlan
from .serializers import ProjectSerializer, AgentSerializer, FloorPlanSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer



