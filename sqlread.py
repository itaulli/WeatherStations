import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta


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

#accepts a weather tuple and returns the datetime string
def datestr(tup):
    out = tup[0][0:4]+tup[0][5:7]+tup[0][8:10]+tup[0][11:13]+tup[0][14:16]
    return out

#makes a plot of the temperature for the entire rawlist
def tempplot(rawlist):
    xlist = []
    ylist = []
    labels = []
    
    for entry in rawlist:
        datetime = int(datestr(entry))
        xlist.append(datetime)
        ylist.append(entry[2])
        label = entry[0][0:16]
        labels.append(label)
        
    sparselabels = ['']*len(labels)
    sparselabels[0::15] = labels[0::15]
    nat = np.arange(len(ylist))
    
    plt.figure(num=None, figsize=(3*6.4,3*4.8), dpi=300)
    plt.plot(nat,ylist)
    plt.xticks(nat, sparselabels, rotation='vertical')
    
    ax = plt.gca()
    ax.set_title('Temperature ID: 106')
    ax.set_xlabel('date/time')
    ax.set_ylabel('Temperature (C)')
    plt.savefig('tempplot.pdf')
    
    

database = "/home/teststand/SQLite/database/weather.db"
 
conn = create_wal_connection(database)
    
tphlist = db_to_list(conn, 'TPH')

#print(tphlist[-1])
tempplot(tphlist)

