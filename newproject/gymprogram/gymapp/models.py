from django.db import models

class Move(models.Model):
	name = models.CharField(max_length=100)
	reps = models.IntegerField(default=10)
	sets = models.IntegerField(default=4)
	weight = models.FloatField(blank=True, null=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return f"{self.name} | {self.reps} | {self.sets} | {self.weight} | {self.description}"

class Program(models.Model):
	name = models.CharField(max_length=100)
	info = models.TextField(blank=True)
	move = models.ManyToManyField("Move")

	def __str__(self):
		return self.name	

	class Meta:
		ordering = ["name"]
