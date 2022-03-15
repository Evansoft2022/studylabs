from django.db import models

class Post(models.Model):
	title = models.CharField(max_length = 150)
	description = models.CharField(max_length = 150)
	content = models.TextField()
	img = models.ImageField(upload_to = 'Post')
	new = models.BooleanField(default=True)

