# Generated by Django 5.2 on 2025-04-16 21:46

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_remove_project_gallery_alter_agent_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Téléphone'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='bathrooms',
            field=models.IntegerField(verbose_name='Salles de bain'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='bedrooms',
            field=models.IntegerField(verbose_name='Chambres'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floor_plans', to='projects.project', verbose_name='Projet'),
        ),
        migrations.AlterField(
            model_name='floorplan',
            name='size',
            field=models.CharField(max_length=50, verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='projects.project', verbose_name='Projet'),
        ),
        migrations.AlterField(
            model_name='project',
            name='about_text',
            field=models.TextField(verbose_name='À propos'),
        ),
        migrations.AlterField(
            model_name='project',
            name='agent',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.agent', verbose_name='Agent'),
        ),
        migrations.AlterField(
            model_name='project',
            name='amenities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None, verbose_name='Équipements'),
        ),
        migrations.AlterField(
            model_name='project',
            name='bathrooms',
            field=models.IntegerField(verbose_name='Salles de bain'),
        ),
        migrations.AlterField(
            model_name='project',
            name='bedrooms',
            field=models.IntegerField(verbose_name='Chambres'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='features',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None, verbose_name='Caractéristiques'),
        ),
        migrations.AlterField(
            model_name='project',
            name='full_description',
            field=models.TextField(verbose_name='Description complète'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='lat',
            field=models.FloatField(verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='project',
            name='lng',
            field=models.FloatField(verbose_name='Longitude'),
        ),
        migrations.AlterField(
            model_name='project',
            name='location',
            field=models.CharField(max_length=200, verbose_name='Emplacement'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='project',
            name='nearby_amenities',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None, verbose_name='Équipements à proximité'),
        ),
        migrations.AlterField(
            model_name='project',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Prix'),
        ),
        migrations.AlterField(
            model_name='project',
            name='property_type',
            field=models.CharField(max_length=100, verbose_name='Type de propriété'),
        ),
        migrations.AlterField(
            model_name='project',
            name='size',
            field=models.FloatField(verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(max_length=100, verbose_name='Statut'),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, size=None, verbose_name='Tags'),
        ),
    ]
