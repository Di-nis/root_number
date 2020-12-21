from rest_framework import serializers


class InputNumberSerializer(serializers.Serializer):
    input_number = serializers.IntegerField(min_value=0)
