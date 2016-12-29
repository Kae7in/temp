from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
	name = models.CharField(max_length=128, blank=False)


class Post(models.Model):
	title = models.CharField(max_length=256, blank=False)
	body = models.TextField(default='', blank=False)
	date_created = models.DateField(auto_now_add=True)
	tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # TODO: Conditionally cascade delete ONLY if this is the last post referencing that tag

	creator = models.ForeignKey(User, related_name='posts', blank=False)


class Comment(models.Model):
	creator = models.OneToOneField(User, related_name='comments')
	post = models.OneToOneField(Post, related_name='comments', blank=False, on_delete=models.CASCADE)

	date_created = models.DateField(auto_now_add=True)
	body = models.TextField(default='', blank=False)




#############################################
# class Item(models.Model):
# 	name = models.CharField(max_length=128, blank=False)
# 	description = models.TextField(default='')
# 	price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=False)
#
# 	owner = models.ForeignKey(User, related_name='items', blank=False)


# class UserProfile(models.Model):
# 	user = models.OneToOneField(User)
# 	username_validator = ASCIIUsernameValidator()
#
#
# class Order(models.Model):
# 	item = models.OneToOneField(Item, on_delete=models.CASCADE)
#
# 	order_date = models.DateField(auto_now_add=True)
# 	ship_date = models.DateField(null=True)
# 	estimated_arrival_date = models.DateField(null=True)
# 	fulfilled = models.BooleanField(default=False)
#
# 	active_orders = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='active_orders', null=True)
# 	fulfilled_orders = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='fulfilled_orders',
# 										 null=True)
