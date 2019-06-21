import logging
import os
import re
import uuid
from datetime import datetime

import gensim
import numpy as np
import spacy
from apscheduler.schedulers.background import BackgroundScheduler
from joblib import parallel_backend
from nltk.corpus import stopwords
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

from topic_modeler import TRAIN_TASK
from topic_modeler.models import RunningTasks, DataRaw, TrainData, TopicModel, Topic, TopicWord

logger = logging.getLogger(__name__)

# define bad symbols
BAD_SYMBOLS_RE = re.compile(r'\W|\d|\.|x{2,}|,|\'')

# define stop words
STOPWORDS = set(stopwords.words('english'))

# Initialize spacy en model
NLP = spacy.load('en')

# keeping only Noun, Adj, Verb, Adverb
ALLOWED_POSTAGS = ['NOUN', 'ADJ', 'VERB', 'ADV']


# does schedule model training
def schedule_train_topic_model(number_of_topics, words_per_topic):
    try:
        # what there
        existing_task = RunningTasks.objects.all().filter(name=TRAIN_TASK)
        # any exist
        if len(existing_task) == 0:
            # create new one
            task = RunningTasks()
            task.name = TRAIN_TASK
            task.running = False
            task.save()
        # load task as one exist already
        existing_task = RunningTasks.objects.all().filter(name=TRAIN_TASK).first()
        # lock check
        if not existing_task.running:
            # lock the task
            existing_task.running = True
            existing_task.save()
            # start background job now
            scheduler = BackgroundScheduler()
            scheduler.add_job(train_topic_model, 'date', args=[number_of_topics, words_per_topic],
                              next_run_time=datetime.now())
            scheduler.start()
            # done
            return 'Model training scheduled'
        return 'Model training already running'
    except:
        # on any exception unlock
        process_task(False)


def extract_topic():
    pass


# does model training
def train_topic_model(number_of_topics, words_per_topic):
    try:
        # do the raw data
        clean_data = process_raw_data()
        # do the features
        clean_lemma_data_vect, clean_lemma_data_vect_features = extract_features(clean_data)
        # do the train
        model_new = train_store_model(number_of_topics, clean_lemma_data_vect)
        # do the topics and words
        process_topics_words(model_new, clean_lemma_data_vect_features, words_per_topic)
    except Exception as e:
        logger.debug(e)
    finally:
        # unlock after done
        process_task(False)


# does topics and words
def process_topics_words(model_new, features, words_count):
    # convert to numpy array
    keywords = np.array(features)
    # da keywords
    topic_keywords = []
    # iterate
    for topic_weights in model_new.model.components_:
        # find the best
        top_keyword_locs = (-topic_weights).argsort()[:int(words_count)]
        # store
        topic_keywords.append(keywords.take(top_keyword_locs))
    # deactivate all other topics
    for t in Topic.objects.filter(inuse=True):
        t.inuse = False
        t.save()
    # deactivate all words
    for t in TopicWord.objects.filter(inuse=True):
        t.inuse = False
        t.save()
    # store in db
    for kw in topic_keywords:
        # topic
        t = Topic()
        t.model = model_new
        t.inuse = True
        t.topic = uuid.uuid1()
        t.save()
        t.refresh_from_db()
        # words
        for wrd in kw:
            w = TopicWord()
            w.topic = t
            w.inuse = True
            w.word = wrd
            w.save()

# does model training
def train_store_model(number_of_topics, data):
    # number of jobs
    jobs_num = os.getenv('LDA_JOBS') if os.getenv('LDA_JOBS') else 1
    # paralell train
    with parallel_backend('threading', n_jobs=jobs_num):
        # LDA train BoW
        lda_vec = LatentDirichletAllocation(n_components=int(number_of_topics), learning_method='online',
                                            n_jobs=jobs_num)
        # train
        lda_vec_trained = lda_vec.fit_transform(data)
        # mark other as not use
        for m in TopicModel.objects.all():
            m.inuse = False
            m.save()
        # store new one
        model_new = TopicModel()
        model_new.perplexity = lda_vec.perplexity(data)
        model_new.decomposition = 'LatentDirichletAllocation'
        model_new.features_extraction = 'CountVectorizer'
        model_new.inuse = True
        model_new.model = lda_vec
        model_new.fitted_model = lda_vec_trained
        model_new.save()
        # reload for an id
        model_new.refresh_from_db()
        # done
        return model_new


# does process raw data
def process_raw_data():
    # for further use
    data_clean = []
    # get all new raw data
    for rd in DataRaw.objects.all():
        # stop words
        cd = basic_clean(rd)
        # store
        data_clean.append(cd)
    # split words
    cd_w = list(sent_to_words(data_clean))
    # lemma
    clean_data = lemma_clean(cd_w)
    # store as clean
    for s in clean_data:
        train_data = TrainData()
        train_data.text = s
        train_data.save()
    # remove all process data
    DataRaw.objects.all().delete()
    # all clean data
    all_clean = []
    # get all old train data
    for td in TrainData.objects.all():
        all_clean.append(td.text)
    # done
    return all_clean


# does feature extraction
def extract_features(clean_lemma_data):
    if len(clean_lemma_data) > 0:
        # create BoW
        vectorised = CountVectorizer(analyzer='word', token_pattern=r'\w{3,}')
        # fit and transform
        clean_lemma_data_vect = vectorised.fit_transform(clean_lemma_data)
        # labels generated
        clean_lemma_data_vect_features = vectorised.get_feature_names()
        # done
        return clean_lemma_data_vect, clean_lemma_data_vect_features


# does updating train task running state
def process_task(running):
    # load task
    existing_task = RunningTasks.objects.all().filter(name=TRAIN_TASK).first()
    # update running state
    existing_task.running = running
    # save
    existing_task.save()


# does basic clean
def basic_clean(data):
    # lower case
    text = str.lower(data.text)
    # remove bad symbols
    text = BAD_SYMBOLS_RE.sub(' ', text)
    # remove stop words and words with length < 2
    text = ' '.join(w for w in text.split() if w not in STOPWORDS and len(w) > 2)
    # done
    return text


# does lemma
def lemma_clean(data):
    # what goes out
    texts_out = []
    # iterate
    for sent in data:
        # doc
        doc = NLP(" ".join(sent))
        # process
        texts_out.append(" ".join(
            [token.lemma_ if token.lemma_ not in ['-PRON-'] else '' for token in doc if token.pos_ in ALLOWED_POSTAGS]))
    # done
    return texts_out


# tokenize each sentence into a list of words
def sent_to_words(sentences):
    for sentence in sentences:
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))
