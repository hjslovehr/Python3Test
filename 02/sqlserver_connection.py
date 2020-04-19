# import pymssql
# DeprecationWarning: Using or importing the ABCs from 'collections' 
# instead of from 'collections.abc' is deprecated, and in 3.8 it will 
# stop working
import pymssql
import sys
sys.path.append('common')
import helpers

server = '123.56.96.237'
database = 'DFMSDB'
user = 'sa'
password = 'Simp2014'


# con = pymssql.connect(server=server, \
#                         user=user, \
#                         password=password, \
#                         database=database)
# cur = con.cursor()
# s = 'SELECT * FROM BASE_PERSON'
# cur.execute(s)

# 一次获取所有数据
# r = cur.fetchall()
# print(r)

# 一行一行循环遍历
# while True:
#     r = cur.fetchone()
#     if None == r:
#         break
#     print(r)


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

@helpers.func_use_time
def test_query_all():
    con = get_connection(server, database, user, password)
    res = get_all(con, 'SELECT * FROM BASE_PERSON')
    con.close()
    # print(res)
    # print(res[0])
    for item in res[0]:
        print(item)


if __name__ == "__main__":
    test_query_all()


