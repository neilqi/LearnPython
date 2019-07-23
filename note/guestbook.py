#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shelve
from flask import Flask, request, render_template, redirect, escape, Markup
from datetime  import datetime

DATA_FILE = 'guestbook.dat'
application = Flask(__name__)

def save_data(name, comment, create_at):
    database = shelve.open(DATA_FILE)
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        greeting_list = database['greeting_list']

    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at
    })

    database['greeting_list'] = greeting_list
    database.close()

def load_data():
    database = shelve.open(DATA_FILE)
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list


@application.route('/')
def index():
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

if __name__ == '__main__':
    application.run('127.0.0.1', 8000, debug=True)

@application.route('/post',method=['POST'])
def post():
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = request.form.get('create_at')
    save_data(name, comment, create_at)
    return redirect('/')

@application.template_filter('nl2br')
def nl2br_filter(s):
    return escape(s).replace('\n', Markup('<br>'))

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    return dt.strftime('%Y/%m/%d %H:%M:%S')