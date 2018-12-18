import os
import sqlite3
import textwrap

class SqlManager():

    def __init__(self, database_path):

        self.database_path = database_path


    def sql_query(self, query, variables=None, get_id=False, specific_database=None):

        database = self.database_path if not specific_database else specific_database

        connection = sqlite3.connect("file:" + database, uri=True)
        cursor = connection.cursor()

        if variables:
            cursor.execute(query, variables)
        else:
            cursor.execute(query)
        rows = cursor.fetchall()
        connection.commit()
        connection.close()

        if get_id:
            return cursor.lastrowid

        return rows

    def clean_table(self, table):
        
        query = textwrap.dedent(
        '''
        DELETE FROM %s
        ''' % (table))
        self.sql_query(query)


    def clean_integrations(self):
        self.clean_table('integration')

    def clean_queries(self):
        self.clean_table('query')