import sqlite3
from collections import namedtuple

Uni = namedtuple('Uni', ['id', 'name'])
Degree = namedtuple('Degree', ['id', 'name', 'cs'])

def get_unis(conn):
    c = conn.cursor()

    unis = []
    for uni in c.execute('SELECT id, name FROM unis'):
        unis.append(Uni(*uni))

    return unis

def get_degrees(conn):
    c = conn.cursor()

    degrees = []
    for degree in c.execute('SELECT id, name, cs FROM degrees'):
        degrees.append(Degree(*degree))

    return degrees

def submit_student(conn, name, years_stud, years_tutor, uni, degree):
    c = conn.cursor()

    # Add the person into the database
    c.execute('INSERT INTO ncsser (name, uni, degree) VALUES (?, ?, ?)', (name, uni, degree))
    personid = c.lastrowid

    # And add the years into the database as well!
    for year in years_stud:
        c.execute('INSERT INTO years (ncssid, year, tutor) VALUES (?, ?, 0)', (personid, year,))
    for year in years_tutor:
        c.execute('INSERT INTO years (ncssid, year, tutor) VALUES (?, ?, 1)', (personid, year,))

    conn.commit()

def connect():
    return sqlite3.connect('ncss.db')
