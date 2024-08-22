from rest_framework import serializers
from stock.models import StockLocation


class StockLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockLocation
        fields = ["id", "name", "address", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_name(self, value):
        if StockLocation.objects.filter(name=value).exists():
            raise serializers.ValidationError("Un emplacement avec ce nom existe déjà.")
        return value
