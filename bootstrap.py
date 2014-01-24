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
    c.execute('CREATE TABLE ncss_unis (id INTEGER PRIMARY KEY AUTOINCREMENT, ncssid INTEGER, uni INTEGER);')
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
    unis = ['Australian Catholic Uni',
            'Australian National Uni',
            'Bond Uni',
            'Central QLD Uni',
            'Charles Darwin Uni',
            'Charles Stuart Uni',
            'Curtin Uni',
            'Edith Cowan Uni',
            'Flinders Uni',
            'Griffith Uni',
            'James Cook Uni',
            'La Trobe',
            'Macquarie',
            'Monash',
            'Murdoch Uni',
            'QUT',
            'RMIT',
            'Southern Cross',
            'Swinbourne',
            'Adelaide',
            'Ballarat',
            'Canberra',
            'Melbourne',
            'New England',
            'UNSW',
            'UTas',
            'USyd',
            'UWS',
            'UOW',
            'UWA']
    unis = [(uni,) for uni in unis]

    c = conn.cursor()
    c.executemany('INSERT INTO unis (name) VALUES (?)', unis)
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
