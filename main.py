import sqlite3
from bottle import get, post, request, route, run, jinja2_template

import database

@route('/')
def main():
    return jinja2_template('index.html')

@get('/ncsser')
def ncsser():
    conn = database.connect()
    context = {}

    context['unis'] = database.get_unis(conn)
    context['degrees'] = database.get_degrees(conn)

    return jinja2_template('ncsser.html', context)

@post('/ncsser')
def post_ncsser():
    redirect('/')

if __name__ == '__main__':
    run(host='localhost', port=8080)
