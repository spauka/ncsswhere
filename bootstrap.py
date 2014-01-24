import os
import sqlite3

# Create an empty database
def create(conn):
    c = conn.cursor()
    # Create the ncsser table
    c.execute('CREATE TABLE ncsser (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT);')

    # Store the years people attended
    c.execute('CREATE TABLE years (id INTEGER PRIMARY KEY AUTOINCREMENT, ncssid INTEGER, year INTEGER, tutor INTEGER);')

    # Store the unis/degrees that people attended/did
    c.execute('CREATE TABLE ncss_unis (id INTEGER PRIMARY KEY AUTOINCREMENT, ncssid INTEGER, uni INTEGER, lat REAL, lng REAL);')
    c.execute('CREATE TABLE ncss_degrees (id INTEGER PRIMARY KEY AUTOINCREMENT, ncssid INTEGER, degree INTEGER);')

    # Create a table of universities
    c.execute('CREATE TABLE unis (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, lat REAL, lng REAL)')

    # Create a table of degrees
    c.execute('CREATE TABLE degrees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, cs INTEGER)')

    conn.commit()

    # Populate the initial list
    populate_unis(conn)
    populate_degrees(conn)

def populate_unis(conn):
    unis = [('Australian Catholic University', -33.836683,151.20389),
            ('Australian National University', -35.277647,149.118627),
            ('Bond University', -28.072681,153.416902),
            ('Central QLD University', -23.322888,150.520867),
            ('Charles Darwin University', -12.371778,130.868987),
            ('Charles Stuart University', 43.357887,-79.787482),
            ('Curtin University', -32.006256,115.894515),
            ('Edith Cowan University', -31.919166,115.869109),
            ('Flinders University', 0,0),
            ('Griffith University', 0,0),
            ('James Cook University', 0,0),
            ('La Trobe Univerist', 0,0),
            ('Macquarie University', 0,0),
            ('Monash University', 0,0),
            ('Murdoch University', 0,0),
            ('Qeensland University of Technoloty', 0,0),
            ('RMIT University', 0,0),
            ('Southern Cross University', 0,0),
            ('Swinburne University of Technology', 0,0),
            ('University of Adelaide', 0,0),
            ('University of Ballarat', 0,0),
            ('University of Canberra', 0,0),
            ('University of Melbourne', 0,0),
            ('University of New England', 0,0),
            ('University of UNSW', -31.919166,115.869109),
            ('University of Tasmania', -42.90181,147.327598),
            ('University of Sydney', -33.889922,151.190604),
            ('University of Technology Sydney', -33.883955,151.201054),
            ('University of Western Sydney', 0,0),
            ('University of Woollongong', 0,0),
            ('University of Western Australian', 0,0),
            ('Victoria University', 0,0),
            ('Other', 0,0),
           ]
    unis = [(uni, lat, lng) for uni, lat, lng in unis]

    c = conn.cursor()
    c.executemany('INSERT INTO unis (name, lat, lng) VALUES (?, ?, ?)', unis)
    conn.commit()

def populate_degrees(conn):
    degrees = [('Computer Science', True),
              ('Computer Engineering', True),
              ('IT', True),
              ('Physics', False),
              ('Chemistry', False),
              ('Biology', False),
              ('Mathematics', False),
              ('Other Science', False),
              ('Mechanical Engineering', False),
              ('Electrical Engineering', False),
              ('Mechatronics', False),
              ('Other Engineering', False),
              ('Arts', False),
              ('Other', False),
             ]

    c = conn.cursor()
    c.executemany('INSERT INTO degrees (name, cs) VALUES (?, ?)', degrees)
    conn.commit()

if __name__ == '__main__':
    if os.path.exists('ncss.db'):
        confirm = ''
        print 'Warning: The database already exists and will be cleared! Please confirm (Yes or No)'
        while confirm != 'Yes':
            confirm = raw_input('Yes or No? ')
            if confirm == 'No':
                exit(0)
        os.remove('ncss.db')

    conn = sqlite3.connect('ncss.db')
    create(conn)
    conn.close()
