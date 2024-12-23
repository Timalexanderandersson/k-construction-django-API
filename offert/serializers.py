from rest_framework import serializers
from .models import Offert


class OffertSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Offert
        fields = "__all__"