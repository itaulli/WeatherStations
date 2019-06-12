import time
import zmq
import sqlite3
from sqlite3 import Error
"""
The reciever must already be running before the sender is started
"""

#the function that recieves data
#saves incoming dictionary as "data"
def consumer():
    print("Reciever is operational")
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://129.118.107.227:5556")

    data = consumer_receiver.recv_json()
    print("Recieved data from weather station {}".format(data['idnum'],))
    return data

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

#function to add a TPH entry to the database
def add_TPH(conn, TPH):
    """
    Add another data point to the TPH table
    :param conn:
    :param TPH:
    :return:
    """
    sql = ''' INSERT INTO TPH(id, temperature, pressure, humidity)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, TPH)
    return cur.lastrowid

#function to add a PC entry to the database
def add_PC(conn, PC):
    """
    Create a new task
    :param conn:
    :param PC:
    :return:
    """
 
    sql = ''' INSERT INTO PC(id, "0.3um", "0.5um", "1.0um", "2.5um", "5.0um", "10.0um")
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, PC)
    return cur.lastrowid

#function to report data to the database
def push_data(data):
    database = "/home/teststand/SQLite/database/weather.db"
 
    #unpack the data dictionary
    idnum = int(data['idnum'])
    temp = int(data['temp'])
    press = int(data['pressure'])
    hum = int(data['humidity'])
    pc003 = int(data['part'][0])
    pc005 = int(data['part'][1])
    pc010 = int(data['part'][2])
    pc025 = int(data['part'][3])
    pc050 = int(data['part'][4])
    pc100 = int(data['part'][5])

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new TPH entry
        TPHrow = (idnum, temp, press, hum);
        add_TPH(conn, TPHrow)
        
        #create a new PC entry
        PCrow = (idnum, pc003, pc005, pc010, pc025, pc050, pc100)
        add_PC(conn, PCrow)
    print("database updated successfully")

#get the data from the weather station and make the report
while True:
    data = consumer()
    push_data(data)
