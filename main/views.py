import django_filters.rest_framework
from rest_framework import viewsets

from .models import User, Task, Tag
from .serializers import UserSerializer, TaskSerializer, TagSerializer


class UserFilter(django_filters.FilterSet):
    """Filter User instances by name."""
    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ("name",)


class TaskFilter(django_filters.FilterSet):
    """Filter Task instances by tags, status, author, and executor."""
    tags = django_filters.ModelMultipleChoiceFilter(
        field_name="tags__name",
        to_field_name="name",
        queryset=Tag.objects.order_by("id"),
    )
    status = django_filters.ChoiceFilter(choices=Task.status.choices)
    author = django_filters.ModelChoiceFilter(queryset=User.objects.order_by("id"))
    executor = django_filters.ModelChoiceFilter(queryset=User.objects.order_by("id"))

    class Meta:
        model = Task
        fields = (
            "tags",
            "status",
            "author",
            "executor",
        )


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TaskViewSet:
    queryset = Task.objects.order_by("id")
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet:
    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer
