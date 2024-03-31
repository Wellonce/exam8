from rest_framework import serializers
from task3.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["price", "marja", "package_code"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        instance.set_encrypted_fields(
            data["price"], data["marja"], data["package_code"]
        )
        return instance.get_decrypted_fields()
