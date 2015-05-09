__author__ = 'zuoyun1'

# import sys
#
#
# print(sys.path)

import MySQLdb

db=None
cur=None

try:
    db = MySQLdb.connect("localhost", "root", "", "dmj_trades")
    cur = db.cursor()
    cur.execute("show tables")
    # tables=cur.fetchmone()
    # tables=cur.fetchmany(5)
    tables=cur.fetchall()

    for table in tables:
        print(table[0])



except MySQLdb.Error, e:
    print "mysql error %d: %s", e.args[0], e.args[1]

finally:
    if db or cur:
        cur.close()
        db.close()

    print("over")



