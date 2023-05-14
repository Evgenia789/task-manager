from rest_framework import serializers

from .models import User, Tag, Task


class UserSerializer(serializers.ModelSerializer):
    """The UserSerializer serializer for the User model."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone",
        )


class TagSerializer(serializers.ModelSerializer):
    """The TagSerializer serializer for the Tag model."""

    class Meta:
        model = Tag
        fields = ("id", "name")


class TaskSerializer(serializers.ModelSerializer):
    """The TaskSerializer serializer for the Task model."""

    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "description",
            "created_date",
            "updated_date",
            "deadline",
            "status",
            "priority",
            "author",
            "executor",
            "tags",
        )

    def create(self, validated_data):
        """
        The `create` method for creating object.
        """
        tags = validated_data.pop("tags", None)
        task = Task.objects.create(**validated_data)
        if tags is not None:
            task.tags.set(tags)

        return task

    def update(self, instance, validated_data):
        """
        The `update` method for editing object.
        """
        tags = validated_data.pop("tags", None)
        if tags is not None:
            instance.tags.set(tags)
        Task.objects.filter(pk=instance.pk).update(**validated_data)
        instance.refresh_from_db()
        return instance
