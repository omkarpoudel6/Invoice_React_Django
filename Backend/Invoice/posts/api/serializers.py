from rest_framework import serializers
from ..models import Post

class PostModelSerializer(serializers.ModelSerializer):

    author=serializers.SerializerMethodField()
    created_at=serializers.SerializerMethodField()

    class Meta:
        model=Post
        fields=['id','title','description','created_at','author']

    
    def get_author(self,obj):
        print(self)
        print(obj)
        return obj.author.username

    def get_created_at(self,obj):
        return obj.created_at.strftime('%m-%d-%y, %H:%M:%S')