from django.db import models

class Question_P(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text


class Choice_P(models.Model):
	question = models.ForeignKey('Question_p', on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=10)
	def __str__(self):
		return self.choice_text

