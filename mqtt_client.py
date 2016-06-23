import sys
import paho.mqtt.publish as publish
import random
import demjson
import time

def transmitMQTT(strMsg):
    #strMqttBroker = "localhost"
    strBroker = "123.56.201.7"
    strMqttChannel = "environment"
    #print(strMsg)
    publish.single(strMqttChannel, strMsg, hostname = strBroker)

if __name__ == '__main__':
    data = {}
    while True:
        temperature = random.randint(-20,50)
        #data["temperature"] = temperature
        print temperature
        hcho_concentrer = random.uniform(0.001,1)
        #data["hcho_concentrer"] = hcho_concentrer
        print hcho_concentrer
        rh = random.randint(0,100)
        print rh
        pm_one_point_five = random.randint(1,120)
        print pm_one_point_five
        pm_one = random.randint(1,120)
        print pm_one
        pm_ten = random.randint(1,120)
        data = str(temperature)+","+str(rh)+","+str(hcho_concentrer)+","+str(pm_one_point_five)+","+str(pm_one)+","+str(pm_ten)
        transmitMQTT(data)
        print "Send msg ok."
        time.sleep(15)