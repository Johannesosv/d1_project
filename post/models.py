from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(default=datetime.now,blank=True)
    #Becomes a table in the database
	def __str__(self):
		return self.title
    #class Meta:
    #    verbose_name_plural="Posts" #Gör inget, men visar att man manuellt kan ändra namnet