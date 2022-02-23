from django.db import models

# Create your models here.
class Leads(models.Model):
    title = models.CharField(max_length=20)
    details = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Leads'

    def __str__(self):
        return self.title + ' || ' + str(self.pk) 
