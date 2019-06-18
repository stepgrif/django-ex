from django.db import models


# the root
class TopicModel(models.Model):
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(default=None, blank=True, null=True)
    perplexity = models.FloatField(default=None, blank=True, null=True)
    decomposition = models.CharField(max_length=250, default=None, blank=True, null=True)
    features_extraction = models.CharField(max_length=250, default=None, blank=True, null=True)
    inuse = models.BooleanField()
    fitted_model = models.BinaryField(default=None, blank=True, null=True)


# topics of the model
class Topic(models.Model):
    model = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    topic = models.CharField(max_length=50)
    inuse = models.BooleanField()


# words of the topics
class TopicWord(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    word = models.CharField(max_length=50)
    inuse = models.BooleanField()


# topic extraction job
class TopicExtractionJob(models.Model):
    model = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(default=None, blank=True, null=True)
    reference = models.CharField(max_length=250)
    processed = models.BooleanField()
    text = models.TextField()
