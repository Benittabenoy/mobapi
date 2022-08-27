from rest_framework import serializers

class ClotheSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField(max_length=120)
    brand=serializers.CharField()
    material=serializers.CharField()
    size=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

