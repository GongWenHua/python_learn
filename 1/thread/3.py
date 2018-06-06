import os
import random
import time
from multiprocessing import Process, Queue


# 写入数据
def write(q):
    print('Processing to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to Queue ' % value)
        q.put(value)
        time.sleep(random.random())


# 读取数据
def read(q):
    print('Processing to read: %s' % os.getpid())
    while True:
        value = q.get(True)  # 阻塞读取
        print('Read %s from Queue ' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
