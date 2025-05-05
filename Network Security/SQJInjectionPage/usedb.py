from pathlib import Path
import os
from os import getcwd
from os.path import join

import sqlite3

def filedir():
    # https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory
    # https://stackoverflow.com/questions/1592565/determine-if-variable-is-defined-in-python
    try:
        return Path(__file__).parent.absolute()
    except:
        # in case __file__ doesn't exist (probably running from a shell)
        return getcwd()

def sql_serialize(value):
    # mette le virgolette sulle stringhe per non interpretarle come variabili
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)

class WorkerDB:
    # https://flask.palletsprojects.com/en/stable/tutorial/database/
    # https://docs.python.org/3/library/sqlite3.html
    def __init__(self):
        self.db_conn = self.db_connect(join(filedir(), 'db.sqlite'))

    def look_for_firstname(self, value):
        cur = self.db_conn.cursor()
        return cur.execute(
            f"""SELECT * FROM Workers
            WHERE firstname = {sql_serialize(value)}"""
        ).fetchall()

    def gendb(self):
        conn = sqlite3.connect(join(filedir(), 'db.sqlite'),
                               detect_types=sqlite3.PARSE_DECLTYPES,
                               check_same_thread=False)
        current_directory = os.path.dirname(os.path.abspath(__file__))
        schema_path1 = os.path.join(current_directory, 'schema.sql')
        schema_path2=os.path.join(current_directory,'populate.sql')

        with open(schema_path1, encoding='utf-8') as f:
            conn.executescript(f.read())
        with open(schema_path2, encoding='utf-8') as f:
            conn.executescript(f.read())

    def look_for_lastname(self, value):
        cur = self.db_conn.cursor()
        return cur.execute(
            f"""SELECT * FROM Workers
            WHERE lastname = {sql_serialize(value)}"""
        ).fetchall()

    def look_for_both(self, firstname, lastname):
        cur = self.db_conn.cursor()
        res = cur.execute(
            f"""SELECT * FROM Workers
            WHERE firstname = {sql_serialize(firstname)}
            and lastname = {sql_serialize(lastname)}"""
        )
        return res.fetchall()

    def db_connect(self, db_path):
        try:
            connection = sqlite3.connect(db_path, check_same_thread=False)
            print("Database connection established.")
            return connection
        except sqlite3.Error as e:
            print(f"Database connection failed: {e}")
            raise
    def insert(self, firstname, lastname):
        cur = self.db_conn.cursor()
        return cur.executescript(
            f"""INSERT into Workers(lastname, firstname)
            values({sql_serialize(lastname)}, {sql_serialize(firstname)})"""
        )

    # per debugging
    def get_all(self):
        cur = self.db_conn.cursor()
        res = cur.execute('select * from Workers')
        return res.fetchall()

    def print_all(self):
        for row in self.get_all():
            for item in row:
                print(item, end=', ')
            print('')


