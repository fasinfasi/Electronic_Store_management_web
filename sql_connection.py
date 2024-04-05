import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='#P8J99G2GJfasin',
                                host='127.0.0.1',
                                database='electronic_store')
    return __cnx
