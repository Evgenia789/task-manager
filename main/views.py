import django_filters.rest_framework
from rest_framework import viewsets

from .models import User, Task, Tag
from .permissions import DeletePermission
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
    status = django_filters.ChoiceFilter(choices=Task.Statuses.choices)
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
    """A viewset for CRUD operations on User instance."""

    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    filterset_class = UserFilter


class TaskViewSet(viewsets.ModelViewSet):
    """A viewset for CRUD operations on Task instance."""

    queryset = Task.objects.order_by("id")
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
    permission_classes = (DeletePermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class TagViewSet(viewsets.ModelViewSet):

    """A viewset for CRUD operations on Tag instance."""

    queryset = Tag.objects.order_by("id")
    serializer_class = TagSerializer
    permission_classes = (DeletePermission,)
