from django.db import models
from datetime import datetime
from django.utils import timezone


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=200)
    job_text = models.CharField(max_length=200)
    date = models.DateTimeField('date')
    pub_date = models.DateTimeField('date published', auto_now_add=True)


    def __str__(self):
        return self.job_title


class Volunteer(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    volunteer_name = models.CharField(max_length=100)
    volunteer_email = models.EmailField(max_length=100)
    volunteer_grade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.volunteer_name
