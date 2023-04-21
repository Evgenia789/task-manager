from rest_framework import viewsets

from .models import User, Task, Tag
from .serializers import UserSerializer, TaskSerializer, TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer


class TaskViewSet():
    queryset = Task.objects.order_by("id")
    serializer_class = TaskSerializer


class TagViewSet():
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer
