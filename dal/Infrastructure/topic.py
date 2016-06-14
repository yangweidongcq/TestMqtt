# encoding:utf-8

from peewee import *
from database.DataSource import mqtt_test_database

class UnKnowField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = mqtt_test_database

class Topic(BaseModel):
    id = IntegerField()
    temperature = IntegerField()
    hcho_concentrer = FloatField()
    rh = IntegerField()
    topic_name =CharField()
    create_time = CharField()
    class Meta:
        db_table = 'topic'
