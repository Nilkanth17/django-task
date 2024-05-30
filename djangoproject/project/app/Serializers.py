from rest_framework import serializers

from django.contrib.auth.models import User  ####



from .models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll_number = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

class CreateSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    subcategory = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())

    class Meta:
        model = Student
        fields = ('category', 'subcategory', 'name', 'roll_number', 'city')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class StudentModelSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category')
    subcategory_name = serializers.StringRelatedField(source='subcategory')
 
    class Meta:
        model = Student
        fields = '__all__'

class iteamModelSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(source='category')
    subcategory_name = serializers.StringRelatedField(source='subcategory')
 
    class Meta:
        model = item
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = login_ragister
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'email', 'password')
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()