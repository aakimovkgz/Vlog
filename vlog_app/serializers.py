from rest_framework import serializers
from .models import *


class PostSerializers(serializers.ModelSerializer):
    
    img = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'img', 'description', 'update_date', 'user_id')
        # fields = '__all__'
        # exclude = ('create_date', 'update_date')
        

class MyProfilePostSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'img', 'description', 'is_draft', 'update_date')  
    
    
class PostCreateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'img', 'description', 'is_draft')  
        
        
class PostEditSerializers(serializers.ModelSerializer):
    
    title = serializers.CharField(required=True)
    img = serializers.ImageField(required=False, max_length=None, allow_empty_file=True, use_url=True)
    description = serializers.CharField(required=True)
    is_draft = serializers.BooleanField(required=True)
    is_delete = serializers.BooleanField(required=True)
    
    class Meta:
        model = Post
        fields = ('title', 'img', 'description', 'is_draft', 'is_delete')
        
        
class PostDetailSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('title', 'img', 'description', 'is_draft', 'user_id', 'update_date')
        
        
class ContactSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class SiteInfoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = SiteInfo
        fields = '__all__'
        