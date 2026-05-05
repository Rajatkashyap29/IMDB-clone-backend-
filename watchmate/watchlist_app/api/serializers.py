from rest_framework import serializers
from watchlist_app.models import WactchList ,StreamPlateform,Review,Product,DogCategory

class ProductSeriliazer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
        
class DogSeriliazer(serializers.Serializer):
    class Meta:
        model=DogCategory
        fields="__all__"        
        

class ReviewSeriliazer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        exclude=('wactchList',)
        # fields="__all__"
        
        
class WactchListSerializer(serializers.ModelSerializer):
    reviews=ReviewSeriliazer(many=True ,read_only=True)
    class Meta:
        model=WactchList
        fields="__all__" 

        
class  StreamPlateformSerializers(serializers.ModelSerializer):
    watchlist=WactchListSerializer(many=True,read_only=True)
    # watchlist=serializers.StringRelatedField(many=True,read_only=True)
    # watchlist=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # #watchlist = serializers.HyperlinkedRelatedField(
    #         many=True,
    #         read_only=True,
    #         view_name='movie-detail'  
    #     )    
    class Meta:
        model=StreamPlateform
        fields="__all__"

        # isse hame sare fields milenge 
        # exclude=['active']  jisko htana hai usko aise exclude mai likh do 
        
        
        
        

# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short!")
#     else:
#         return value


# class MovieSerializers(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField(validators=[name_length])
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
        
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name= validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
        
#         instance.save()
#         return instance
    
# # field level validation
#     # def validate_name(self, value):
#     #         if len(value) < 2:
#     #             raise serializers.ValidationError("Name is too short!")
#     #         else:
#     #             return value

    
    
# #obj level validatiion
#     def validate(self,value):
#         if value['name']==value['description']:
#             raise serializers.ValidationError("name and descripton should not same")
#         else:
#             return value   
        
             