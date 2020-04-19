# import pymssql
# DeprecationWarning: Using or importing the ABCs from 'collections' 
# instead of from 'collections.abc' is deprecated, and in 3.8 it will 
# stop working
import pymssql

def get_connection(ser, db, user, pwd):
    return pymssql.connect(ser, user, pwd, db)


def query_scalar(con, sqlstr):
    cur = con.cursor()
    cur.execute(sqlstr)
    return cur.fetchone()[0]


def get_all(con, sqlstr):
    cur = con.cursor()
    cur.execute(sqlstr)
    return cur.fetchall()


def get_cur(con, sqlstr):
    cur = con.cursor()
    cur.execute(sqlstr)
    return cur


