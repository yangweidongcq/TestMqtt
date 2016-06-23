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
    temperature = FloatField()
    hcho_concentrer = FloatField()
    rh = FloatField()
    topic_name =CharField()
    pm_two_point_five = IntegerField()
    pm_one = IntegerField()
    pm_ten = IntegerField()
    create_time = CharField()
    class Meta:
        db_table = 'topic'
