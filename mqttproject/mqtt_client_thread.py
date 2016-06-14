# encoding:utf-8
from Queue import Queue
from threading import Thread
import paho.mqtt.publish as publish
import time
class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            # Get the work from the queue and expand the tuple
            # 从队列中获取任务并扩展tuple
            link = self.queue.get()
            self.queue.task_done()
            strmsg = "Hello,world"
            # strMqttBroker = "localhost"
            strBroker = "123.56.201.7"
            strMqttChannel = "sensor"
            print(strMsg)
            publish.single(strMqttChannel, strmsg, hostname=strBroker)



def main():
    ts = time()
    # Create a queue to communicate with the worker threads
    queue = Queue()
    # Create 8 worker threads
    # 创建八个工作线程
    for x in range(8):
        worker = DownloadWorker(queue)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        # 将daemon设置为True将会使主线程退出，即使worker都阻塞了
        worker.daemon = True
        worker.start()
    # Put the tasks into the queue as a tuple
    # 将任务以tuple的形式放入队列中

    queue.put()
    # Causes the main thread to wait for the queue to finish processing all the tasks
    # 让主线程等待队列完成所有的任务
    queue.join()
    print('Took {}'.format(time() - ts))
if __name__ == "__main__":
    main()