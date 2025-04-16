import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

class Agent(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    
    # Cloudinary image instead of raw URL
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=100)  # Matches frontend ID
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    full_description = models.TextField()
    about_text = models.TextField()

    # Cloudinary image for main cover
    image = CloudinaryField('image')

    # Replace gallery ArrayField with related model below
    # Removed: gallery = ArrayField(models.URLField(), blank=True, default=list)

    tags = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    features = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    amenities = ArrayField(models.CharField(max_length=100), blank=True, default=list)
    nearby_amenities = ArrayField(models.CharField(max_length=200), blank=True, default=list)

    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    property_type = models.CharField(max_length=100)
    size = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    status = models.CharField(max_length=100)

    lat = models.FloatField()
    lng = models.FloatField()

    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = CloudinaryField('image')

    def __str__(self):
        return f"{self.project.name} - Gallery Image"

class FloorPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='floor_plans')
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    size = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.project.name} - {self.name}"
