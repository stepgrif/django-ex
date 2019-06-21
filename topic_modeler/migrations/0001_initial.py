# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-21 12:27
from __future__ import unicode_literals

import django.db.models.deletion
import picklefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataRaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RunningTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('running', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(max_length=50)),
                ('inuse', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TopicExtractionJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('reference', models.CharField(max_length=250)),
                ('processed', models.BooleanField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TopicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('perplexity', models.FloatField(blank=True, default=None, null=True)),
                ('decomposition', picklefield.fields.PickledObjectField(editable=False)),
                ('features_extraction', picklefield.fields.PickledObjectField(editable=False)),
                ('inuse', models.BooleanField()),
                ('model', picklefield.fields.PickledObjectField(editable=False)),
                ('fitted_model', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='TopicWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('word', models.CharField(max_length=50)),
                ('inuse', models.BooleanField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic_modeler.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='TrainData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='topicextractionjob',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic_modeler.TopicModel'),
        ),
        migrations.AddField(
            model_name='topic',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic_modeler.TopicModel'),
        ),
    ]
