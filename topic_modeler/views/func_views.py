from django.http import HttpResponse

from topic_modeler.topic_modeler import TopicModeler

modeler = TopicModeler()


def train_model(request):
    # extract parameters
    number_of_topics = request.GET['number_of_topics']
    words_per_topic = request.GET['words_per_topic']
    # schedule job
    message = modeler.schedule_train_topic_model(number_of_topics, words_per_topic)
    # done
    return HttpResponse(message)


def extract_topic(request):
    # extract parameters
    text = request.GET['text']
    # schedule job
    message = modeler.do_topic_extraction(text)
    # done
    return HttpResponse(message)
