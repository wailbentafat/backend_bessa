from django.contrib import admin
from .models import Contact, Project, Agent, FloorPlan, GalleryImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class FloorPlanInline(admin.StackedInline):
    model = FloorPlan
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline, FloorPlanInline]
    list_display = ('name', 'location', 'price', 'status')
    search_fields = ('name', 'location', 'status')

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email')
    search_fields = ('name', 'title', 'email')

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('project',)

@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'bedrooms', 'bathrooms')
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)