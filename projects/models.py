import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

class Agent(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom")
    title = models.CharField(max_length=100, verbose_name="Titre")
    phone = models.CharField(max_length=50, verbose_name="Téléphone")
    email = models.EmailField(verbose_name="Email")
    
    # Cloudinary image instead of raw URL
    image = CloudinaryField('image', blank=True, null=True)  # No verbose_name here

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.CharField(primary_key=True, max_length=100, verbose_name="ID")  # Matches frontend ID
    name = models.CharField(max_length=200, verbose_name="Nom")
    location = models.CharField(max_length=200, verbose_name="Emplacement")
    description = models.TextField(verbose_name="Description")
    full_description = models.TextField(verbose_name="Description complète")
    about_text = models.TextField(verbose_name="À propos")

    # Cloudinary image for main cover
    image = CloudinaryField('image')  # No verbose_name here

    tags = ArrayField(models.CharField(max_length=50), blank=True, default=list, verbose_name="Tags")
    features = ArrayField(models.CharField(max_length=100), blank=True, default=list, verbose_name="Caractéristiques")
    amenities = ArrayField(models.CharField(max_length=100), blank=True, default=list, verbose_name="Équipements")
    nearby_amenities = ArrayField(models.CharField(max_length=200), blank=True, default=list, verbose_name="Équipements à proximité")

    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)], verbose_name="Prix")
    property_type = models.CharField(max_length=100, verbose_name="Type de propriété")
    size = models.FloatField(verbose_name="Taille")
    bedrooms = models.IntegerField(verbose_name="Chambres")
    bathrooms = models.IntegerField(verbose_name="Salles de bain")
    status = models.CharField(max_length=100, verbose_name="Statut")

    lat = models.FloatField(verbose_name="Latitude")
    lng = models.FloatField(verbose_name="Longitude")

    agent = models.OneToOneField(Agent, on_delete=models.CASCADE, verbose_name="Agent")

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images', verbose_name="Projet")
    image = CloudinaryField('image')  # No verbose_name here

    def __str__(self):
        return f"{self.project.name} - Image de galerie"

class FloorPlan(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='floor_plans', verbose_name="Projet")
    name = models.CharField(max_length=100, verbose_name="Nom")
    image = CloudinaryField('image')  # No verbose_name here
    size = models.CharField(max_length=50, verbose_name="Taille")
    bedrooms = models.IntegerField(verbose_name="Chambres")
    bathrooms = models.IntegerField(verbose_name="Salles de bain")
    description = models.TextField(verbose_name="Description")

    def __str__(self):
        return f"{self.project.name} - {self.name}"
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"