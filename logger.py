#~/usr/bin/env python
#store level in database
import sqlite3

dbname='level.db'

def log_level(level):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO level values(datetime('now'), (?))", (temp,))

    conn.commit()

    conn.close()
