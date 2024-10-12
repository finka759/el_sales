from rest_framework import serializers

from networkapp.models import Product, Link, Contact


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор продукта"""

    class Meta:
        model = Product
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор контакта"""

    class Meta:
        model = Contact
        fields = "__all__"


class LinkSerializer(serializers.ModelSerializer):
    """Сериализатор звена"""

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ['supplier_debt', ]
