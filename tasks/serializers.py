from rest_framework import serializers
from tasks.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    """
    Tasks Serializer.

    Used to serialize the Tasks model to JSON. The fields to be
    serialized are:
    - id
    - title
    - description
    - status
    - updated
    """

    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'status', 'updated')