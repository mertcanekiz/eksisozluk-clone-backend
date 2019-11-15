from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Thread

class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    author = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    # thread = serializers.HyperlinkedRelatedField(view_name='thread-detail', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

class ThreadSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ['id', 'url', 'title', 'posts']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = '__all__'
