import sqlite3


def checkDataBase(data, table):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    if(data.keys() > 0):
        where = " WHERE"    
        i = 0
        for e in data.keys():
            i+=1
            where += f" {e} = {data[e].value} "
            where += "AND" if i != len(data.keys()) else ""

    toExecute = f"""
        SELECT * from {table}
    """ + where
    cursor.execute(toExecute)
    users = cursor.fetchall()
    conn.close()
    return users

def updateDataBaseById(data, table, id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    toExecute = f"""
        UPDATE {table}
        SET
    """
    for e in data.keys():
        i+=1
    

def createDataBase(data, table):
    conn = sqlite3.connect('databes.db')
    cursor = conn.cursor()
    toExecute = f"""
        CREATE TABLE IF NOT EXISTS {table}(
            id INTEGER PRIMARY KEY AUTOINCREMENT
    """
    for e in data:
        toExecute = f", {e.name} {e.type} "

    toExecute += ")"
    cursor.execute(toExecute)
    conn.commit()
    conn.close()