from rest_framework import serializers
from orders.models import User, Post, Comment, Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
	posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'posts')


class PostSerializer(serializers.HyperlinkedModelSerializer):
	creator_username = serializers.ReadOnlyField(source='creator.username')
	creator_link = serializers.HyperlinkedIdentityField(view_name='user-detail')
	post_comments = serializers.ReadOnlyField(source='comments')

	class Meta:
		model = Post
		fields = ('url', 'id', 'date_created', 'title', 'body', 'creator_username', 'creator_link', 'post_comments', 'tags')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	creator_username = serializers.ReadOnlyField(source='creator.username')
	creator_link = serializers.HyperlinkedIdentityField(view_name='user-detail')

	class Meta:
		model = Comment
		fields = ('url', 'id', 'date_created', 'body', 'creator_username', 'creator_link')


class TagSerializer(serializers.HyperlinkedModelSerializer):
	posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

	class Meta:
		model = Tag
		fields = ('url', 'id', 'name', 'posts')


#########################################
# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	# items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
# 	items = serializers.HyperlinkedRelatedField(many=True, view_name='item-detail', read_only=True)
#
# 	class Meta:
# 		model = User
# 		fields = ('url', 'id', 'username', 'items')
#
#
# class ItemSerializer(serializers.HyperlinkedModelSerializer):
# 	owner_username = serializers.ReadOnlyField(source='owner.username')
# 	owner_link = serializers.HyperlinkedIdentityField(view_name='user-detail')
#
# 	class Meta:
# 		model = Item
# 		fields = ('url', 'id', 'name', 'description', 'price', 'owner_link', 'owner_username')
