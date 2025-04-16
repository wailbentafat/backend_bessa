from rest_framework import serializers
from .models import Project, Agent, FloorPlan

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name', 'title', 'phone', 'email', 'image']

class FloorPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorPlan
        fields = ['id', 'name', 'image', 'size', 'bedrooms', 'bathrooms', 'description']

class ProjectSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    floor_plans = FloorPlanSerializer(many=True)
    gallery = serializers.ListField(child=serializers.URLField())

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'location', 'description', 'full_description', 'about_text',
            'image', 'gallery', 'tags', 'features', 'amenities', 'nearby_amenities',
            'price', 'property_type', 'size', 'bedrooms', 'bathrooms', 'status',
            'lat', 'lng', 'agent', 'floor_plans'
        ]
