from django.db import models

class Poll(models.Model):
	title = models.CharField(max_length=250)
	created_at = models.DateTimeField(auto_now=True)

class Choice(models.Model):
	poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=250)
	votes = models.IntegerField(default=0)
