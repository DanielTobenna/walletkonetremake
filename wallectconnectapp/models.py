from django.db import models

# Create your models here.

class MetaMaskseed(models.Model):
	seed_id = models.AutoField(primary_key=True, null=False)
	seed= models.TextField(max_length= 5000, null=False)

	def __str__(self):
		return self.seed
