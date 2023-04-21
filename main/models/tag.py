from django.db import models


class Tag(models.Model):
    """
    Model representing a tag.

    Attributes:
        name (str): The name of the tag.
    """

    name = models.CharField(max_length=200, null=True, blank=False)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name
