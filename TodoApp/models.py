from django.db import models


# Create your models here.
class Task(models.Model):
    status = (
        ("complete", "Complete"),
        ("in_progress", "In Progress"),
    )
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True, verbose_name="Description")
    status = models.CharField(max_length=200, choices=status)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
