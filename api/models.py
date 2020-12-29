from django.db import models

class CoronaVirus(models.Model):

    country             = models.CharField(max_length=50)
    total_cases         = models.CharField(max_length=50)
    new_cases           = models.CharField(max_length=50)
    total_deaths        = models.CharField(max_length=50)
    new_deaths          = models.CharField(max_length=50)
    total_recovered     = models.CharField(max_length=50)
    active_cases        = models.CharField(max_length=50)
    total_tests         = models.CharField(max_length=50)
    population          = models.CharField(max_length=50)
    continent           = models.CharField(max_length=50)
    slug                = models.SlugField(blank= True)
    
    class Meta:
        verbose_name = "coronavirus"
        verbose_name_plural = "coronavirus"

    def __str__(self):
        return self.country

