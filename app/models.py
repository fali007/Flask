import sqlite3

class DB:
    def __init__(self):
        try:
            self.conn=sqlite3.connect('income.db')
            cursor=self.conn.cursor()
            print("Database created successfully and connected to SQlite")
            cursor.execute("select sqlite_version();")
            record=cursor.fetchall()
            print("Version is :", record)
            cursor.close()
        except sqlite3.Error as error:
            print("Error")

    def create_table(self):
        print("Creating new table")
        query = '''CREATE TABLE income (
                name TEXT NOT NULL,
                date datetime,
                amount REAL NOT NULL);'''
        cursor=self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        print("Created table ")
        cursor.close()
    
    def insert_table(self,name,time,amount):
        print("Instering into database")
        query='''INSERT INTO income
        (name, date,amount)
        VALUES (?,?,?);
        '''
        cursor=self.conn.cursor()
        cursor.execute(query,(name,time,amount))
        self.conn.commit()
        print("Inserted ",cursor.rowcount)
        cursor.close()

    def update_table(self,amount,date,name):
        print("Updating table")
        cursor=self.conn.cursor()
        query='''Update income set amount = ?,date=? where name=?'''
        cursor.execute(query,(amount,date,name))
        self.conn.commit()
        cursor.close()
        print("Updated the row")

    def delete(self,name):
        print("Deleting table")
        cursor=self.conn.cursor()
        query='''DELETE from income where name=?'''
        cursor.execute(query,(name,))
        self.conn.commit()
        cursor.close()
        print("Deleted successfully")

    def fetch(self):
        cursor=self.conn.cursor()
        cursor.execute('SELECT * FROM income')
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        return rows

class DB_e:
    def __init__(self):
        try:
            self.conn=sqlite3.connect('expense.db')
            cursor=self.conn.cursor()
            print("Database created successfully and connected to SQlite")
            cursor.execute("select sqlite_version();")
            record=cursor.fetchall()
            print("Version is :", record)
            cursor.close()
        except sqlite3.Error as error:
            print("Error")

    def create_table(self):
        print("Creating new table")
        query = '''CREATE TABLE expense (
                name TEXT NOT NULL,
                date datetime,
                amount REAL NOT NULL);'''
        cursor=self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        print("Created table ")
        cursor.close()
    
    def insert_table(self,name,time,amount):
        print("Instering into database")
        query='''INSERT INTO expense
        (name, date,amount)
        VALUES (?,?,?);
        '''
        cursor=self.conn.cursor()
        cursor.execute(query,(name,time,amount))
        self.conn.commit()
        print("Inserted ",cursor.rowcount)
        cursor.close()

    def update_table(self,amount,date,name):
        print("Updating table")
        cursor=self.conn.cursor()
        query='''Update expense set amount = ?,date=? where name=?'''
        cursor.execute(query,(amount,date,name))
        self.conn.commit()
        cursor.close()
        print("Updated the row")

    def delete(self,name):
        print("Deleting table")
        cursor=self.conn.cursor()
        query='''DELETE from expense where name=?'''
        cursor.execute(query,(name,))
        self.conn.commit()
        cursor.close()
        print("Deleted successfully")

    def fetch(self):
        cursor=self.conn.cursor()
        cursor.execute('SELECT * FROM expense')
        rows=cursor.fetchall()
        for row in rows:
            print(row)
        cursor.close()
        return rows