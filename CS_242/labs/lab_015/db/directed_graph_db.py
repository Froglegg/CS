import sqlite3


def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except:
        print(
            f"Something went wrong trying to connect to the db file {dbFile}")
    return conn


def createTable(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS graphs
                (id integer PRIMARY KEY, graphLabel text NOT NULL, graphData json)''')


def readTable(conn):
    cur = conn.cursor()
    # table is an iterable of rows
    table = cur.execute('SELECT * FROM graphs')
    return [row for row in table]


def insertIntoTable(conn, data):
    params = (data[0], data[1])

    sql = '''INSERT INTO graphs(graphLabel,graphData) 
             VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    print(f"{params[0]} added to DB")


def updateTable(conn, data):
    ''' params are label, json data, ID'''
    params = (data[0], data[1], data[2])
    sql = f''' UPDATE graphs
                SET graphLabel = ? ,
                    graphData = ? 
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    print(f"{params[0]} updated in DB")


def deleteFromTable(conn, graphId: int):
    # remember the tuple gotcha, gotta have that comma!
    # PS second argument in cur.execute must be tuple type
    params = (graphId,)
    sql = ''' DELETE FROM graphs
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    print(f"Entry with ID: {graphId} removed from DB")
