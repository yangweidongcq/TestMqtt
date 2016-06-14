# encoding:utf-8
import threading, urllib2
import datetime, time
import Queue
import paho.mqtt.publish as publish


class ThreadClass(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            strMsg = "hello,world"
            strBroker = "123.56.201.7"
            strMqttChannel = "sensor"
            publish.single(strMqttChannel, strMsg, hostname=strBroker)


def main():
    queue = Queue.Queue()
    for i in range(200):
        t = ThreadClass(queue)
        # 主程序退出时，子线程也立即退出
        t.setDaemon(True)
        # 启动线程
        t.start()
    for j in range(200):
        queue.put(j)
        # 向队列中填充数数
    queue.join()
if __name__ == '__main__':
    st = time.time()
    main()
    print '%f' % (time.time() - st)