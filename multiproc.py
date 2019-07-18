#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 1. 使用fork() 方法， windows系统不支持
# print('Process (%s) start...' % os.getpid())

# pid = os.fork()
# if pid == 0:
#     print('I am a child process (%s) and my perent is %s' % (os.getpid(), os.getppid))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# 2. 使用 Process
from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s (%s)... ' % (name, os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     print('Child process will start')
#     p = Process(target=run_proc, args=('test', )) #创建子进程，指定执行函数和参数
#     p.start()       #启动进程
#     p.join()        #等待子进程结束后再继续执行
    
#     print('Child process end.')

# 3. 使用进程池Pool
from multiprocessing import Pool
import os, time, random

# def long_time_task(name):
#     print('run task %s (%s)...' %(name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(2)             # 允许同时跑2个进程
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))       #启动异步进程
#     print('Waiting for all subprocess done...')
#     p.close()       #在调用join之前需先调用close。调用完close就不能再创建新进程
#     p.join()        #等待所有子进程执行完毕。
#     print('all process done')

# 4. subprocess模块用于控制子进程
import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code: ', r)

# print('$nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, 
# stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')

# # communicate 相当于提供交互模式下输入的内容
# print(output)
# print('exit code:', p.returncode)


# 5. 进程间通信

from multiprocessing import Process, Queue

def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q, ))
    pr = Process(target=read, args=(q, ))
    #start pw, begin to write
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()

