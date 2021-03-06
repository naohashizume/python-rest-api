# create_tables.py
#
# Create table
#
# Author:  Nao Hashizume, Matt Harrison Set 2B

import sqlite3

conn = sqlite3.connect('readings.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE temperature_reading
          (id INTEGER PRIMARY KEY ASC,
           timestamp DATETIME NOT NULL,
           model VARCHAR(250) NOT NULL,
           min_reading FLOAT(3) NOT NULL,
           avg_reading FLOAT(3) NOT NULL,
           max_reading FLOAT(3) NOT NULL,
           status VARCHAR(250) NOT NULL
          )
          ''')
c.execute('''
          CREATE TABLE pressure_reading
          (id INTEGER PRIMARY KEY ASC,
           timestamp DATETIME NOT NULL,
           model VARCHAR(250) NOT NULL,
           min_reading FLOAT(3) NOT NULL,
           avg_reading FLOAT(3) NOT NULL,
           max_reading FLOAT(3) NOT NULL,
           status VARCHAR(250) NOT NULL
          )
          ''')

conn.commit()
conn.close()
