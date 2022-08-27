from rest_framework import serializers
from mobapi.models import mobiles
class MobileSerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField(max_length=120)
    brand=serializers.CharField()
    band=serializers.CharField()
    display=serializers.CharField()
    price=serializers.IntegerField()
    rating=serializers.FloatField()

class MobileModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=mobiles
        fields="__all__"
        # fields=["name","brand","band","display","price","rating"]
