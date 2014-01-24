import sqlite3
from bottle import *
import json

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

@get('/api/ncsser')
def get_ncssers():
    # Set headers
    response.set_header('Content-Type', 'application/json')

    conn = database.connect()
    c = conn.cursor()

    # First get a list of all NCSSers
    ncssers = {}
    for ncsser in c.execute('SELECT * FROM ncsser'):
        ncssers[ncsser[0]] = database.NCSSer(ncsser[0], ncsser[1], [], [], [], [])
    # Fill in the years
    for year in c.execute('SELECT ncssid, year, tutor FROM years'):
        if year[2]:
            ncssers[year[0]].years_tut.append(year[1])
        else:
            ncssers[year[0]].years_stud.append(year[1])
    # And the degrees and unis
    for uni in c.execute('SELECT nu.ncssid, u.name FROM ncss_unis nu INNER JOIN unis u ON nu.uni = u.id'):
        ncssers[uni[0]].unis.append(uni[1])
    for degree in c.execute('SELECT nd.ncssid, d.name FROM ncss_degrees nd INNER JOIN degrees d ON nd.degree = d.id'):
        ncssers[degree[0]].degrees.append(degree[1])

    return json.dumps([ncsser._asdict() for ncsser in ncssers.values()])

@get('/api/unis')
def get_unis():
    # Set headers
    response.set_header('Content-Type', 'application/json')

    conn = database.connect()
    unis = database.get_unis(conn)

    return json.dumps({uni.name: uni._asdict() for uni in unis})

@post('/degree')
def add_degree():
    degree = request.forms.get('degree')
    if not degree:
        redirect('/')
        return

    conn = database.connect()
    c = conn.cursor()
    c.execute('INSERT INTO degrees (name, cs) VALUES (?, 0)', (degree, ))
    conn.commit()

    return "Added %s to the DB"

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
