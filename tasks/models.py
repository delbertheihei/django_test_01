from django.db import models


class Status(models.TextChoices):
    UNSTARTED = 'u', 'Not started yet!'
    ONGOING = 'o', 'On going'
    FINISHED = 'f', 'Finished'


class Task(models.Model):
    name = models.CharField(max_length=65, verbose_name='Task name', unique=True)
    status = models.CharField(max_length=1, verbose_name='Task status', choices=Status.choices)

    def __str__(self):
        return self.name
