# from orders.models import Item, User
from orders.models import User, Post, Comment, Tag
from orders.serializers import UserSerializer, PostSerializer, CommentSerializer, TagSerializer
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from orders.permissions import IsOwnerOrReadOnly



@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-list', request=request, format=format),
		'posts': reverse('post-list', request=request, format=format),
	})


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(creator=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def perform_create(self, serializer):
		serializer.save(creator=self.request.user)


class CommentDetail(generics.RetrieveDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer


class TagList(generics.ListCreateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer

	def perform_create(self, serializer):
		serializer.save(creator=self.request.user)


class TagDetail(generics.RetrieveDestroyAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


###########################################################
# @api_view(['GET'])
# def api_root(request, format=None):
# 	return Response({
# 		'users': reverse('user-list', request=request, format=format),
# 		'items': reverse('item-list', request=request, format=format)
# 	})
#
#
# class UserList(generics.ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer
#
#
# class ItemList(generics.ListCreateAPIView):
# 	queryset = Item.objects.all()
# 	serializer_class = ItemSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
# 	def perform_create(self, serializer):
# 		serializer.save(owner=self.request.user)
#
#
# class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Item.objects.all()
# 	serializer_class = ItemSerializer
# 	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
