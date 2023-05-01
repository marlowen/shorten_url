from django.db import models
from django.urls import reverse
import datetime

class Listurls(models.Model):

    fecha = models.DateTimeField("Fecha")
    urloriginal = models.CharField("Url original", max_length=300, blank=True, null=True,)
    urlcorto = models.CharField("Url acortado", max_length=50, blank=True, null=True, unique=True)

    def get_absolute_url(self):
        return reverse("shorten:urlcorto", args=[self.urlcorto])
    
    def save(self, *args, **kwargs):
        self.fecha = datetime.datetime.now()
        super().save(*args, **kwargs)