import sqlite3
from collections import namedtuple

Uni = namedtuple('Uni', ['id', 'name', 'lat', 'lng'])
Degree = namedtuple('Degree', ['id', 'name', 'cs'])
NCSSer = namedtuple('NCSSer', ['id', 'name', 'years_stud', 'years_tut', 'unis', 'degrees'])

def get_unis(conn):
    c = conn.cursor()

    unis = []
    for uni in c.execute('SELECT id, name, lat, lng FROM unis'):
        unis.append(Uni(*uni))

    return unis

def get_degrees(conn):
    c = conn.cursor()

    degrees = []
    for degree in c.execute('SELECT id, name, cs FROM degrees'):
        degrees.append(Degree(*degree))

    return degrees

def submit_student(conn, name, years_stud, years_tutor, unis, degrees):
    c = conn.cursor()

    # Check if the person is already in the DB
    count = list(c.execute('SELECT * FROM ncsser WHERE name LIKE ?', (name,)))
    if len(count):
        return False

    # Add the person into the database
    c.execute('INSERT INTO ncsser (name) VALUES (?)', (name,))
    personid = c.lastrowid

    # Add unis and degrees
    for uni in unis:
        c.execute('INSERT INTO ncss_unis (ncssid, uni) VALUES (?, ?)', (personid, uni))
    for degree in degrees:
        c.execute('INSERT INTO ncss_degrees (ncssid, degree) VALUES (?, ?)', (personid, degree))

    # And add the years into the database as well!
    for year in years_stud:
        c.execute('INSERT INTO years (ncssid, year, tutor) VALUES (?, ?, 0)', (personid, year,))
    for year in years_tutor:
        c.execute('INSERT INTO years (ncssid, year, tutor) VALUES (?, ?, 1)', (personid, year,))

    conn.commit()
    return True

def connect():
    return sqlite3.connect('ncss.db')
