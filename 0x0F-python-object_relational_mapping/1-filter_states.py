#!/usr/bin/python3
import sys
import MySQLdb
'''A script that lists all states from the database that begins with capital "N" hbtn_0e_0_usa.
   It allows 3 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name'''

conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]);
cur = conn.cursor();

cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC") 
for state in cur.fetchall():
    print(state)

