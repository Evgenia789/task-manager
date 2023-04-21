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

    def create(self, validated_data):
        """
        The `create` method for creating object.
        """
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        The `update` method for editing object.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class TaskSerializer(serializers.ModelSerializerd):
    """The TaskSerializer serializer for the Task model."""

    status = serializers.MultipleChoiceField()
    author = UserSerializer()
    executor = UserSerializer()
    tag = TagSerializer(many=True, required=False)

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
            "tag",
        )

    def create(self, validated_data):
        """
        The `create` method for creating object.
        """
        tags = validated_data.pop("tags")
        task = Task.objects.create(**validated_data)
        task.tags.set(tags)
        return task

    def update(self, instance, validated_data):
        """
        The `update` method for editing object.
        """
        tags = validated_data.pop("tags")
        instance.tags.set(tags)
        Task.objects.filter(pk=instance.pk).update(**validated_data)
        instance.refresh_from_db()
        return instance
