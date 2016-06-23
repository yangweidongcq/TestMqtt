#! /usr/bin/python
# enconding:utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import datetime
import time
from dal.Infrastructure.topic import Topic
from common.createredis import create_redis
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git")
    print("cd org.eclipse.paho.mqtt.python")
    print("sudo python setup.py install")


# ======================================================
def on_connect(mqttc, obj, rc):
    print("OnConnetc, rc: " + str(rc))


def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print("Log:" + string)


def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    on_exec(str(msg.payload))


def on_exec(strcmd):
    print "Exec:", strcmd
    strExec = strcmd
    create_redis(strExec)
    data = strExec.split(",")
    temperature = data[0]
    print temperature
    hcho_concentrer = data[2]
    print hcho_concentrer
    rh = data[1]
    print  rh
    pm_one_point_five = data[3]
    print pm_one_point_five
    pm_one = data[4]
    print pm_one
    pm_ten = data[5]
    print pm_ten
    topic_name = "sensor"
    create_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    print create_time
    Topic.create(
        temperature =temperature ,
        hcho_concentrer = hcho_concentrer,
        rh = rh,
        topic_name = topic_name,
        pm_two_point_five = pm_one_point_five,
        pm_one = pm_one,
        pm_ten = pm_ten,
        create_time =create_time
    )

# =====================================================
if __name__ == '__main__':
    mqttc = mqtt.Client("mynodeserver")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log

    strBroker = "123.56.201.7"

    mqttc.connect(strBroker, 1883, 60)
    mqttc.subscribe("sensor", 0)
    mqttc.loop_forever()