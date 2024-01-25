from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
	""" Topic to be inputed by user """
	text = models.CharField(max_length = 200)
	date_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	
	def __str__(self):
		""" return a string represetation of model"""
		return self.text
		
class Entry(models.Model):
	""" Description of the topic learned """
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add = True)
	
	class Meta:
		verbose_name_plural = 'entries'
	
	def __str__(self):
		""" return string version """
		return self.text[:50] + "..."
			

