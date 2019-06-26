from django.http import HttpResponse
from django.shortcuts import render

from topic_modeler.forms import UploadFileForm
from topic_modeler.topic_modeler import TopicModeler, update_topic_description, handle_file_upload

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


def update_topic_descrition(request):
    # extract parameters
    description = request.GET['description']
    topic_uuid = request.GET['topic_uuid']
    # update topic
    message = update_topic_description(description, topic_uuid)
    # done
    return HttpResponse(message)


def upload_file(request):
    # for post
    if request.method == 'POST':
        # construct form
        form = UploadFileForm(request.POST, request.FILES)
        # is file populated
        if form.is_valid():
            # process
            message = handle_file_upload(request.FILES['file'])
            # done
            return HttpResponse(message)
    # empty form
    return render(request, 'topic_modeler/data_upload.html', {'form': UploadFileForm()})
