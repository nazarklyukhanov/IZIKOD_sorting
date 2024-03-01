import sqlite3


class DataDriver:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS logins (id INTEGER PRIMARY KEY, login TEXT)')

    def insert_data(self, login):
        self.cursor.execute('INSERT INTO logins (login) VALUES (?)', (login,))
        self.conn.commit()

    def get_data(self):
        self.cursor.execute('SELECT * FROM logins')
        return self.cursor.fetchall()
    def close_connection(self):
        self.conn.close()
