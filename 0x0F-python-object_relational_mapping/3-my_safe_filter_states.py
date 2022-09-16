#!/usr/bin/python3
import sys
import MySQLdb
'''A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa 
   where name matches the argument. It takes 4 arguments - 1st arg = user
                                                         - 2nd arg = passwd
                                                         - 3rd arg = database_name
                                                         - 4th = name of state'''

conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]);
cur = conn.cursor();
cur.execute("SELECT * FROM states");
for state in cur.fetchall():
    if(state[1] == sys.argv[4]):
        print(state)
