#~/usr/bin/env python
#store level in database
import sqlite3

dbname='fuellog.db'

def log_level(level):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO level values(datetime('now'), (?))", (level,))

    conn.commit()

    conn.close()
