from rest_framework import serializers
from django.contrib.auth.models import User

from blog_api.models import Post, Comment, Category, PostImages


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')


# ____________________________________________________________________________________________________________________

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'parent')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation


# exists - проверяет есть или нет объекты

class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImages
        exclude = ('id', )


# ___________________________________________________________________________________________________________________

class PostSerializer(serializers.ModelSerializer):
    # source --> через него получаем конкретно от кого берем посты
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
    images = PostImageSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'owner', 'comments', 'category','preview', 'images')


# serializer --- нужен для того, чтобы менять формат текста из query_set в dictionary и из него в json
# ___________________________________________________________________________________________________________________


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'body', 'owner', 'post')
