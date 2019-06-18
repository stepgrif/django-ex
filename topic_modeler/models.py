from django.db import models

# Create your models here.

class TopicModel(models.Model):
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    perplexity = models.FloatField()
    decomposition = models.CharField(max_length=250)
    features_extraction = models.CharField(max_length=250)
    fitted_model = models.BinaryField()

