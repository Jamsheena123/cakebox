from rest_framework import serializers
from delight.models import User,cakes,cakevarients,carts,orders,offers,reviews

class Userserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["id","username","email","password","phone","address"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class CakevarientSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=cakevarients
        exclude=("cake",)      
    
class Cakeserializer(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(read_only=True,slug_field="name")
    varient=CakevarientSerializer(many=True,read_only=True)

    class Meta:
        model=cakes
        fields="__all__"  

class  OfferSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    cakevarient=serializers.CharField(read_only=True)
    price=serializers.CharField(read_only=True)
    start_date=serializers.CharField(read_only=True)
    due_date=serializers.CharField(read_only=True)

    class Meta:
        model=offers
        fields=["cakevarient","price","start_date","due_date"]     



class CartSerializer(serializers.ModelSerializer):
    cakevarient=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:    
        model=carts
        fields="__all__"

class OrderSerializer(serializers.ModelSerializer):
    cakevarients=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    ordered_date=serializers.CharField(read_only=True)
    expected_date=serializers.CharField(read_only=True)
    address=serializers.CharField(read_only=True)

    class Meta:
        model=orders
        fields="__all__"

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    cake=serializers.CharField(read_only=True)

    class Meta:
        model=reviews
        fields="__all__"    


