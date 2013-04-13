from django.db import models

# Create your models here.
class Photo(models.Model):
	# photo, engineering, sketch
	category = models.CharField(max_length=30,unique=False)
	subcategory = models.CharField(max_length=30,unique=False)
	title = models.CharField(max_length=50,unique=True)
	filename = models.CharField(max_length=50,unique=True)
	place = models.CharField(max_length=100,unique=False)
	date = models.DateField()

	def __unicode__(self):
		return self.title
