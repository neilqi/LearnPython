#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, threading

# def loop():
#     print('thread %s is running...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s is running...' % threading.current_thread().name)

# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)

# 2. lock 由于多线程中的变量可以共享，可能导致线程中的一个变量被其他变量修改的问题，使用线程锁lock可以避免
# 原理是持有锁的线程才能执行，其他线程等待，知道锁被释放
# 由于锁只有一个，无论多少线程，同一时刻都只有一个线程持有该锁

# balance = 0
# lock = threading.Lock()

# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()

# 3. ThreadLocal

# local_school = threading.local()
# # 全局变量local_school是一个threadlocal对象，每个thread都可以读写
# # 
# def process_student():
#     #获取当前线程关联的student
#     std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()


# 4. 分布式进程
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

def return_task_queue():
    global task_queue
    return task_queue
 
def return_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:



'''
在windows 中不能用lambda：lambda函数不能被pickled
如果在Xnix系统中可以直接使用
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)

如果在windows系统中，需要自行处理callable
'''
if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')

