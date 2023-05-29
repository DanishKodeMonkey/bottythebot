
import psycopg2

import os
from dotenv import load_dotenv

load_dotenv()


LOGIN_HOST = os.getenv('DB_HOST')
LOGIN_DBNAME = os.getenv('DB_NAME')
LOGIN_USER = os.getenv('DB_USER')
LOGIN_PASS = os.getenv('DB_PASS')
LOGIN_PORT = os.getenv('DB_PORT')
DB_CONNECTION_STRING = f"host={LOGIN_HOST} port={LOGIN_PORT} dbname={LOGIN_DBNAME} user={LOGIN_USER} password={LOGIN_PASS}"

def connect():
    #Conenct to postgresql server.

    conn = None

    try:
        print('Connecting to postgreSQL database...')
        #initiate database connection, fill in parameters from config
        with psycopg2.connect(DB_CONNECTION_STRING) as connection:
            with connection.cursor() as cursor:
                print('PostGreSQL database version: ')
                cursor.execute('SELECT version()')
                db_version = cursor.fetchone()
                print(db_version)
                print('Job done, later choom!')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    #And ensure the door is closed so to speak.
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed. Later choom!')

if __name__ == '__main__':
    connect()