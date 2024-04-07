from django.db import models

class Log(models.Model):
    # class Meta:
    #     abstract = True
        
    class Levels(models.TextChoices):
        INFO = 'info', 'Info'
        WARNING = 'warning', 'Warning'
        ERROR = 'error', "Error"

    timestamp = models.DateTimeField()
    level = models.CharField(
        max_length=200,
        blank=False, 
        null=False,
        choices=Levels.choices,
        default=Levels.INFO, 
    )
    message = models.TextField()
