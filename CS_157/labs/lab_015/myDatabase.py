import sqlite3


def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except:
        print(e)
    return conn


def createTable(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id integer PRIMARY KEY, name text NOT NULL, phone text NOT NULL)''')

# setList function


def readTable(conn):
    cur = conn.cursor()
    # table is an iterable of rows
    table = cur.execute('SELECT * FROM contacts')
    return [row for row in table]

# load function


def selectFromTable(conn, contactId):
    cur = conn.cursor()
    params = (contactId)
    sql = '''SELECT FROM contacts WHERE id = ? '''
    return cur.execute(sql, params)

# add function


def insertIntoTable(conn, contact: list):
    params = (contact[0], contact[1])

    sql = '''INSERT INTO contacts(name,phone) 
             VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    print(f"{params} added to DB")

# update function


def updateTable(conn, contact: list):
    params = (contact[0], contact[1], contact[2])
    sql = f''' UPDATE contacts
                SET name = ? ,
                    phone = ? 
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    print(f"{params} updated in DB")

# delete function


def deleteFromTable(conn, contactId: int):
    # remember the tuple gotcha, gotta have that comma!
    # PS second argument in cur.execute must be tuple type
    params = (contactId,)
    sql = ''' DELETE FROM contacts
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    print(f"Entry with ID: {contactId} removed from DB")
