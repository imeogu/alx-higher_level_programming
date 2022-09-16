#!/usr/bin/python3
import sys
import MySQLdb
'''A script that lists all cities from the database hbtn_0e_0_usa.
   It allows 3 arguments - 1st arg = user
                         - 2nd arg = passwd
                         - 3rd arg = database_name'''

conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]);
cur = conn.cursor();

cur.execute("SELECT * FROM cities as c \
    INNER JOIN states as s on c.state_id = s.id ORDER BY c.id ASC") 
for city in cur.fetchall():
        print(city)

