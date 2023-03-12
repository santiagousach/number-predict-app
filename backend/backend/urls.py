from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from main.views import predict_number

# Register API views with the router
router = routers.DefaultRouter()

# Set up schema view and permissions
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for my project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=3600), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=3600), name='schema-redoc'),
    path('predict/', predict_number, name='predict_number'),
]
