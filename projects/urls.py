from django.urls import path
from .views import ProjectListAPIView, ProjectDetailAPIView, contact_submit
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # List of all projects
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),

    # Detail of a single project
    path('projects/<str:id>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    
    # Schema view for OpenAPI documentation
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI documentation
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # ReDoc documentation
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/contact/', contact_submit),
]

