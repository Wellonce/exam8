from django.db import models

# Create your models here.
class Vacancy(models.Model):
    position = models.CharField(max_length = 128)
    desc = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        verbose_name_plural = 'Vacancies'
    
    def __str__(self) -> str:
        return self.position