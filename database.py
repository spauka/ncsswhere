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

def connect():
    return sqlite3.connect('ncss.db')
