# encoding:utf-8
import sys
import datetime
import socket, sys
import paho.mqtt.publish as publish
import time

import threading
import time, random, sys


class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0
    def increment(self):
        self.lock.acquire()
        self.value = value = self.value + 1
        self.lock.release()
        return value
counter = Counter()
cond = threading.Condition()
class Worker(threading.Thread):
    def run(self):
        strMsg = "hello,world"
        strBroker = "123.56.201.7"
        strMqttChannel = "sensor"
        publish.single(strMqttChannel, strMsg, hostname=strBroker)
        print self.getName(), "-- created."
        cond.acquire()
        cond.wait()
        cond.release()


if __name__ == '__main__':

    try:
        for i in range(3500):
            Worker().start()  # start a worker
    except BaseException, e:
        print "异常: ", type(e), e
        time.sleep(5)
        print "maxium i=", i
    finally:
        cond.acquire()
        cond.notifyAll()
        cond.release()
        time.sleep(3)
        print threading.currentThread().getName(), " quit"