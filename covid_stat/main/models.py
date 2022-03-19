from django.db import models

class Stat(models.Model):
    date = models.CharField("date", max_length=11)
    sick = models.CharField("sick", max_length=11)
    sick_change = models.CharField("sick_change", max_length=11)
    healed = models.CharField("healed", max_length=11)
    healed_change = models.CharField("healed_change", max_length=11)

    def __str__(self):
        return self.date


