from .admin import task_manager_admin_site
from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, TagViewSet, TaskViewSet


router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")
router.register(r"tasks", TaskViewSet, basename="tasks")
router.register(r"tags", TagViewSet, basename="tags")

urlpatterns = [
    path("admin/", task_manager_admin_site.urls),
    path("api/", include(router.urls)),
]
