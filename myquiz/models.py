from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_content = models.CharField(max_length=200, default='')
    choice1 = models.CharField(max_length=100, default='')
    choice2 = models.CharField(max_length=100, default='')
    choice3 = models.CharField(max_length=100, default='')
    choice4 = models.CharField(max_length=100, default='')
    answer = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text