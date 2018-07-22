from django.db import models
from django import forms

# Create your models here.

class Reply(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return self.name