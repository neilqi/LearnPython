#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def consumer():
#     r = ''
#     while True:
#         n = yield r     # 3. 通过yield拿到消息；本次循环的结果放到r中，由yield返回
#         if not n:
#             return
#         print('[Consumer] consuming %s' % n)
#         r = '200 OK'    # 4. 这里是本次循环的结果

# def produce(c):
#     c.send(None)        # 1. c就是consumer
#     n = 0
#     while n < 5:
#         n = n+1
#         print('[Producer] producing %s' % n)
#         r = c.send(n)   # 2. 生产了新的n，通过send(n) 切换到consumer
#                         # 5. send的返回就是consumer的处理结果
#         print('[Producer] Consumer return: %s' % r)
#     c.close()           # 6. 关闭consumer，整个过程结束

# c = consumer()
# produce(c)

# 1. asyncio的编程模型是一个消息循环。
# 2. 从async模块中直接获取一个eventloop的引用
# 3. 把需要执行的协程扔到EventLoop中执行，就实现了异步IO

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # yield from: 异步调用asyncio.sleep(1):
    # 当async.sleep返回时，线程就可以从yield from拿到返回值
    # sleep期间，主线程并未等待，而是去执行eventloop中其他可执行的协程
    r = yield from asyncio.sleep(3)
    print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

import threading
import asyncio

# @asyncio.coroutine
# def hello2():
#     print('Hello 2 world (%s)' % threading.currentThread())
#     yield from asyncio.sleep(3)
#     print('Hello 2 again (%s)' % threading.currentThread())

# loop = asyncio.get_event_loop()
# tasks = [hello2(), hello2()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# @asyncio.coroutine
# def wget(host):
#     print('wget %s ...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))

#     writer.close()


# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

import asyncio
from aiohttp import web

async def index(request):
    await asyncio.sleep(1)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    await asyncio.sleep(1)
    text = '<h1>hello, %s!<h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'),  content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9001)
    print('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()