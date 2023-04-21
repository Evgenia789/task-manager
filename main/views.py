from rest_framework import viewsets

from .models import User, Task, Tag
from .serializers import UserSerializer, TaskSerializer, TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TaskViewSet():
    queryset = Task.objects.order_by("id")
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet():
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer
