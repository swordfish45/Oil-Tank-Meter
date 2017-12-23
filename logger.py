#~/usr/bin/env python
#store level in database
import sqlite3

dbname='/usr/lib/cgi-bin/fuellog.db'

def log_level(level):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print level
    curs.execute("INSERT INTO level values(datetime('now'), (?))", (level,))

    conn.commit()

    conn.close()
