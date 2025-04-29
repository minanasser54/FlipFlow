# serializers.py
from rest_framework import serializers
from Item.models import Item ,Category
from Market.models import Transaction
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    item_url = serializers.SerializerMethodField()
    Item_owner= serializers.SlugRelatedField(read_only=True, slug_field='username')
    Item_category = serializers.SlugRelatedField(read_only=True, slug_field='Category_name')
    class Meta:
        model = Item
        fields = [
            'id', 'Item_name', 'Item_img', 'Item_description', 'Item_price',
            'Item_quantity', 'Item_published', 'Item_createdat', 'Item_slug',
            'Item_owner', 'Item_category', 'item_url',
        ]

    def get_item_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/api/items/{obj.id}/')
        return f'/api/items/{obj.Item_slug}/'


class TransactionSerializer(serializers.ModelSerializer):
    transaction_url = serializers.SerializerMethodField()
    user_from = serializers.SlugRelatedField(read_only=True, slug_field='username')
    user_to = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = Transaction
        fields = [
            'id', 'user_from', 'user_to', 'transaction_type', 'transaction_status',
            'amount', 'created_at', 'transaction_url',
        ]


    def get_transaction_url(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f'/api/transactions/{obj.id}/')
        return f'/api/transactions/{obj.id}/'
