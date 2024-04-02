from rest_framework import serializers
from ..models import Carlist,Showroomlist,Review


class ReviewSerializers(serializers.ModelSerializer):
    apiuser=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        exclude=('car',)
        # fields="__all__"

class CarSerializer(serializers.ModelSerializer):
    discounted_price=serializers.SerializerMethodField()
    Reviews=ReviewSerializers(many=True, read_only=True)
    class Meta:
        model=Carlist
        fields="__all__"
        # fields=['name','id','description']
        # exclude=['name']

    def get_discounted_price(self, object):
        discountprice=object.price-5000
        return discountprice
    
    def validate_price(self, value):
        if value<=20000.00:
            raise serializers.ValidationError("Price must be greater than 20000.00")
        return value
    
    def validate(self, data):
        if data['name']==data['description']:
            raise serializers.ValidationError("Name and description must be different")
        return data
    
class ShowroomSerializer(serializers.ModelSerializer):
    # Showrooms=CarSerializer(many=True, read_only=True)
    # Showrooms= serializers.StringRelatedField(many=True)
    # Showrooms= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    Showrooms= serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='car_detail' )
    class Meta:
        model=Showroomlist
        fields='__all__'
    
