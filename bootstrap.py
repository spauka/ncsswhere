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
    c.execute('CREATE TABLE unis (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

    # Create a table of degrees
    c.execute('CREATE TABLE degrees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, cs INTEGER)')

    conn.commit()

    # Populate the initial list
    populate_unis(conn)
    populate_degrees(conn)

def populate_unis(conn):
    unis = [('Australian Catholic Uni', -33.836683,151.20389),
            ('Australian National Uni', -35.277647,149.118627),
            ('Bond Uni', -28.072681,153.416902),
            ('Central QLD Uni', -23.322888,150.520867),
            ('Charles Darwin Uni', -12.371778,130.868987),
            ('Charles Stuart Uni', 43.357887,-79.787482),
            ('Curtin Uni', -32.006256,115.894515),
            ('Edith Cowan Uni', -31.919166,115.869109),
            ('Flinders Uni', 0,0),
            ('Griffith Uni', 0,0),
            ('James Cook Uni', 0,0),
            ('La Trobe', 0,0),
            ('Macquarie', 0,0),
            ('Monash', 0,0),
            ('Murdoch Uni', 0,0),
            ('QUT', 0,0),
            ('RMIT', 0,0),
            ('Southern Cross', 0,0),
            ('Swinbourne', 0,0),
            ('Adelaide', 0,0),
            ('Ballarat', 0,0),
            ('Canberra', 0,0),
            ('Melbourne', 0,0),
            ('New England', 0,0),
            ('UNSW', -31.919166,115.869109),
            ('UTas', -42.90181,147.327598),
            ('USyd', -33.889922,151.190604),
			('University of Technology Sydney', -33.883955,151.201054),
            ('UWS', 0,0),
            ('UOW', 0,0),
            ('UWA', 0,0),
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
              ('Mechanical Engineering', False),
              ('Electrical Engineering', False),
              ('Mecatronics', False),
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
