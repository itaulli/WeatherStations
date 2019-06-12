import sqlite3
from sqlite3 import Error
 


#function which connects to the database
def create_wal_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        conn.cursor().execute("PRAGMA journal_mode=WAL")
        return conn
    except Error as e:
        print(e)
    
    return None
 
#makes each row an element of a list
#each row is represented by a tuple
#table is either 'TPH' or 'PC'
def db_to_list(conn, table):

    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(table))
 
    rows = cur.fetchall()
    
    return rows



database = "/home/teststand/SQLite/database/weather.db"
 
conn = create_connection(database)
    
tphlist = db_to_list(conn, 'TPH')

print(tphlist[-1])