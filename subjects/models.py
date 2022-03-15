from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=50)
	img = models.ImageField(upload_to = "Category",null=True,default = "")

	def __str__(self):
		return self.name

class Subject(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	price = models.CharField(max_length = 10)
	new = models.BooleanField(default = True)
	img = models.ImageField(upload_to = "Img_Subject",null=True,default = "")
	category = models.ForeignKey(Category,on_delete = models.CASCADE)


class SubModules(models.Model):
	video = models.FileField(upload_to = "Videos")
	title = models.CharField(max_length = 150)
	duration = models.CharField(max_length=10)
	subject = models.ForeignKey(Subject,on_delete = models.CASCADE)



