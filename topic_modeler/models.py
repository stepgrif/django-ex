from django.db import models

# tasks
from picklefield import PickledObjectField


class RunningTasks(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=250)
    running = models.BooleanField()


# unprocessed training data
class DataRaw(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


# training data
class TrainData(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


# the root
class TopicModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    perplexity = models.FloatField(default=None, blank=True, null=True)
    decomposition = PickledObjectField()
    features_extraction = PickledObjectField()
    inuse = models.BooleanField()
    model = PickledObjectField()
    fitted_model = PickledObjectField()


# topics of the model
class Topic(models.Model):
    model = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=50)
    inuse = models.BooleanField()


# words of the topics
class TopicWord(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    word = models.CharField(max_length=50)
    inuse = models.BooleanField()


# topic extraction job
class TopicExtractionJob(models.Model):
    model = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    reference = models.CharField(max_length=250)
    processed = models.BooleanField()
    text = models.TextField()
