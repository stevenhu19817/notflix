from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import TrendingViewSet, DetailsViewSet, CastViewSet, VideoViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r"trending", TrendingViewSet)
router.register(r"details", DetailsViewSet)
router.register(r"cast", CastViewSet)
router.register(r"video", VideoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Video Manager API",
        default_version="v1",
        description="Video Manager API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("trending/", TrendingViewSet.as_view({"get": "list"}), name="trending_list"),
    path("details/", DetailsViewSet.as_view({"get": "list"}), name="details_list"),
    path("cast/", CastViewSet.as_view({"get": "list"}), name="cast_list"),
    path("video/", VideoViewSet.as_view({"get": "list"}), name="video_list"),
    path(
        "trending/<int:pk>/",
        TrendingViewSet.as_view({"get": "retrieve"}),
        name="trending_detail",
    ),
    path(
        "details/<int:pk>/",
        DetailsViewSet.as_view({"get": "retrieve"}),
        name="details_detail",
    ),
    path(
        "cast/<int:pk>/",
        CastViewSet.as_view({"get": "retrieve"}),
        name="cast_detail",
    ),
    path(
        "video/<int:pk>/",
        VideoViewSet.as_view({"get": "retrieve"}),
        name="video_detail",
    ),
    path("", include(router.urls)),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
