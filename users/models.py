from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

class UploadModel(models.Model):
	firstName = models.CharField(max_length=50, null=True)
	lastName = models.CharField(max_length=50,null=True)
	title = models.CharField(max_length=50,null=True)
	department = models.CharField(max_length=50,null=True)
	Fileupload = models.FileField(upload_to='uploads',null=True,validators=[FileExtensionValidator(['pdf'],) ])

	def __str__(self):
		return self.firstName
	
	def delete(self,*args,**kwargs):
		self.Fileupload.delete()
		super().delete(*args, **kwargs)

