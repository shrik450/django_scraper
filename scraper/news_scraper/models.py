from django.db import models
from datetime import date

# Create your models here.
class Headline(models.Model):
	text = models.CharField(max_length=255)
	scanned_date = models.DateField(default = date.today())

	def publish(self, text):
		self.text = text
		self.scanned_date = date.today()
		self.save()

	def __str__(self):
		return self.text

class index_value(models.Model):
	value = models.FloatField()
	scanned_date = models.DateField(default = date.today())

	def publish(self, value):
		self.value = value
		self.scanned_date = date.today()
		self.save()

	def __str__(self):
		return str(value)
