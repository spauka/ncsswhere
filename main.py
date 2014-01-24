import sqlite3
from bottle import get, post, request, route, run, jinja2_template, static_file, redirect

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

    conn.close()

    return jinja2_template('ncsser.html', context)

@post('/ncsser')
def post_ncsser():
    # Get the data from the request
    name = request.forms.get('name')
    years_stud = request.forms.getall('years_stud')
    years_tut = request.forms.getall('years_tut')
    unis = request.forms.getall('uni')
    degrees = request.forms.getall('degree')

    # Finally, add data to the DB!
    conn = database.connect()
    success = database.submit_student(conn, name, years_stud, years_tut, unis, degrees)

    if not success:
        return "You're already in the DB!"
    else:
        redirect('/')

# Static files
@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='css')
@route('/fonts/<filename>')
def fonts(filename):
    return static_file(filename, root='fonts')
@route('/js/<filename>')
def js(filename):
    return static_file(filename, root='js')

if __name__ == '__main__':
    run(host='localhost', port=8080)
