import os
import sqlite3

# Create an empty database
def create(conn):
    c = conn.cursor()
    # Create the ncsser table
    c.execute('CREATE TABLE ncsser (name TEXT PRIMARY KEY, years TEXT, uni INTEGER, cs BOOL, degree TEXT);')

    # Create a table of universities
    c.execute('CREATE TABLE unis (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')

    conn.commit()

    # Populate the initial list
    populate_unis(conn)

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
