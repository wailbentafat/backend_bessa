from rest_framework import serializers
from .models import Project, Agent, FloorPlan, GalleryImage

class AgentSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Agent
        fields = ['name', 'title', 'phone', 'email', 'image']

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class GalleryImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = GalleryImage
        fields = ['image']

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class FloorPlanSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = FloorPlan
        fields = [
            'id',
            'name',
            'image',
            'size',
            'bedrooms',
            'bathrooms',
            'description'
        ]

    def get_image(self, obj):
        return obj.image.url if obj.image else None

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    agent = AgentSerializer()
    floorPlans = FloorPlanSerializer(source='floor_plans', many=True)
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'location',
            'description',
            'full_description',
            'about_text',
            'image',
            'gallery',
            'price',
            'property_type',
            'size',
            'bedrooms',
            'bathrooms',
            'status',
            'tags',
            'features',
            'amenities',
            'nearby_amenities',
            'lat',
            'lng',
            'agent',
            'floorPlans'
        ]

    def get_image(self, obj):
        return obj.image.url if obj.image else None

    def get_gallery(self, obj):
        return [img.image.url for img in obj.gallery_images.all()]
class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3)
    email = serializers.EmailField()
    phone = serializers.CharField(min_length=10)
    subject = serializers.CharField(min_length=3)
    message = serializers.CharField(min_length=10)