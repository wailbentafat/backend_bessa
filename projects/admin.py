from django.contrib import admin
from .models import Project, Agent, FloorPlan

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price', 'status', 'image')
    search_fields = ('name', 'location', 'status')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'phone', 'email')
    search_fields = ('name',)

@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'size', 'bedrooms', 'bathrooms', 'image')
    search_fields = ('name', 'project__name')
