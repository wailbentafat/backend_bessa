import cloudinary
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

class Agent(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    image = models.URLField(blank=True, null=True)  # Optional: For agent image URL

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=100)  
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    full_description = models.TextField()
    about_text = models.TextField()

    # CloudinaryField for a single image upload
    image = CloudinaryField('image')

    # ArrayField to store URLs of multiple images for the gallery
    gallery = ArrayField(models.URLField(), blank=True, default=list)

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

    # ForeignKey to link the agent to the project
    agent = models.OneToOneField(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def upload_gallery_images(self, image_urls):
        """Upload multiple images to Cloudinary and save their URLs in the gallery"""
        uploaded_urls = []
        for url in image_urls:
            upload_result = cloudinary.uploader.upload(url)  # Upload to Cloudinary
            uploaded_urls.append(upload_result['secure_url'])  # Save secure URL
        self.gallery = uploaded_urls  # Store URLs in the gallery field
        self.save()  # Save the project with gallery images

class FloorPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='floor_plans')
    name = models.CharField(max_length=100)
    
    # CloudinaryField for floor plan image
    image = CloudinaryField('image')

    size = models.CharField(max_length=50)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.project.name} - {self.name}"
