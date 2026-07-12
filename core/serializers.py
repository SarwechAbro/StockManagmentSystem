from rest_framework import serializers
from .models import Item, category, section, StockIn, StockOut

class ItemSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Item
        fields = ['id', 'name', 'category','category_name', 'quantity']
        extra_kwargs = {'created_at': {'read_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = section
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    section = serializers.CharField(source='section.name', read_only=True)
    item_category = serializers.CharField(source='category.name', read_only=True)
    date_of_entry = serializers.DateField(format="%d/%m/%Y",
                                       input_formats=['%d/%m/%Y'])

    class Meta:
        model = StockIn
        fields = '__all__'

    def create(self, validated_data):
        # Extract item and quantity from validated data
        item = validated_data['item']
        quantity = validated_data['quantity']

        # Update item stock
        item.quantity += quantity
        item.save()

        # Create the invoice
        stock_entry = StockIn.objects.create(**validated_data)
        return stock_entry    

        
class StockOutSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.name', read_only=True)
    section_name = serializers.CharField(source='section.name', read_only=True)
    item_category = serializers.CharField(source='category.name', read_only=True)
    date_of_issue = serializers.DateField(format="%d/%m/%Y",
                                       input_formats=['%d/%m/%Y'])
    class Meta:
        model = StockOut
        fields = '__all__'
    
    def create(self, validated_data):
        # Extract item and quantity from validated data
        item = validated_data['item']
        quantity = validated_data['quantity']

        # Update item stock
        item.quantity -= quantity
        item.save()

        # Create the invoice
        stock_entry = StockOut.objects.create(**validated_data)
        return stock_entry   
