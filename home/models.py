from django.db import models

class Modificate(models.Model):
	title = models.CharField(max_length = 50)
	subtitle = models.CharField(max_length = 150)
	img_fondo = models.ImageField(upload_to = "Img_Fondo")
	logo = models.ImageField(upload_to = "Logo",null=True,blank = True,default="")


class About(models.Model):
	description = models.TextField()
	mission = models.TextField()
	vision = models.TextField()
	objetives = models.TextField()
	learning_title = models.CharField(max_length = 150,default="")
	learning = models.TextField(default = "")
	learning_img_1 = models.ImageField(upload_to = "learning_img",default="")
	learning_img_2 = models.ImageField(upload_to = "learning_img",default="")

class Information(models.Model):
	address = models.CharField(max_length=150)
	phone = models.CharField(max_length = 14)
	email = models.EmailField()








