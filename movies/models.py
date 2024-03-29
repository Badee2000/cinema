from django.db import models

# Create your models here.

STATUS_CHOICES = [
    ('coming_up', 'Coming Up'),
    ('starting', 'Starting'),
    ('running', 'Running'),
    ('finished', 'Finished'),
]


class Movie(models.Model):
    """
    Movie model. 
    """
    name = models.CharField(max_length=255)
    # protagonists = models.CharField(max_length=255)
    protagonists = models.JSONField(default=list)
    poster = models.URLField()
    trailer = models.URLField()
    start_date = models.DateTimeField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='coming_up')
    ranking = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name
