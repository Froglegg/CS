import sqlite3


def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
    except Error as e:
        print(e)
    return conn


def createTable(conn):
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS contacts
                (id integer PRIMARY KEY, name text, phone text)''')


def readTable(conn):
    cur = conn.cursor()
    # table is an iterable of rows
    table = cur.execute('SELECT * FROM contacts')
    print(table)
    return table


def insertIntoTable(conn, contact: list):
    print(contact)
    params = (contact[0], contact[1])
    sql = '''INSERT INTO contacts(name,phone) 
             VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
    # return cur.lastrowid


def updateTable(conn, contact: list, contactId):
    params = (contact[0], contact[1], contactId)
    sql = f''' UPDATE contacts
                SET name = ? ,
                    phone = ? ,
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()


def deleteFromTable(conn, contactId):
    params = (contactId)
    sql = ''' DELETE FROM contacts
                WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, params)
    conn.commit()
