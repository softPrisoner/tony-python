import datetime
# data base oject realationship  mapping
from django.db import models
# thedjango utils  for timezone
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    # This  is the manager for db items
    objects = models.Manager()
    # mapping the object type to database object type1
    question_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now
    # as your known ,there are some setting params for web view
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published Recently?'

# there your object  has  extended the  models.Model to mapping


class Choice(models.Model):
    objects = models.Manager()
    # delete  cascade
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
