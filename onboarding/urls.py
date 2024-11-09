from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger UI를 위한 스키마 뷰 설정
schema_view = get_schema_view(
    openapi.Info(
        title="Onboarding API",
        default_version='v1',
        description="Onboarding 프로젝트 API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dbsdbf95@gmail.com"),
    ),

    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include("accounts.urls")),
    
    # Swagger UI 경로 추가
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]
