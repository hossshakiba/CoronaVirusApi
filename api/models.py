from django.db import models

class CoronaVirus(models.Model):

    country             = models.CharField(max_length=50, default='')
    total_cases         = models.CharField(max_length=50, default='')
    new_cases           = models.CharField(max_length=50, default='')
    total_deaths        = models.CharField(max_length=50, default='')
    new_deaths          = models.CharField(max_length=50, default='')
    total_recovered     = models.CharField(max_length=50, default='')
    active_cases        = models.CharField(max_length=50, default='')
    total_tests         = models.CharField(max_length=50, default='')
    population          = models.CharField(max_length=50, default='')
    continent           = models.CharField(max_length=50, default='')
    slug                = models.SlugField(blank= True)
    
    class Meta:
        verbose_name = "coronavirus"
        verbose_name_plural = "coronavirus"

    def __str__(self):
        return self.country

