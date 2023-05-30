import psycopg2
from psycopg2 import sql
from psql_error_handler import print_psycopg2_exception as psqle
from dotenv import load_dotenv
import os

#Below is an attempt to fetch table status in postgreSQL server

#First, get the login info
load_dotenv()
LOGIN_HOST = os.getenv('DB_HOST')
LOGIN_DBNAME = os.getenv('DB_NAME')
LOGIN_USER = os.getenv('DB_USER')
LOGIN_PASS = os.getenv('DB_PASS')
LOGIN_PORT = os.getenv('DB_PORT')
DB_CONNECTION_STRING = f"host={LOGIN_HOST} port={LOGIN_PORT} dbname={LOGIN_DBNAME} user={LOGIN_USER} password={LOGIN_PASS}"

def table_fetch():
    #First, ask for which table to lookup
    table_name = input("Please input table name to lookup... \n")
    #Next, run the table_name through sql.Identifier
    #sql_id = format(sql.Identifier(table_name))
    #Then, pass identifier into a query, ready to execute
    #It is recommended to use sql.SQL to pass queries to prevent injection attacks.
    sql_fetch_query =  sql.SQL(f"""SELECT * FROM {table_name}""")
    print(sql_fetch_query)
    """
    try:
        #Establish connection, and notify of connection success.
        conn = psycopg2.connect(DB_CONNECTION_STRING)
        print("Connecting...")
        print(f"psycopg2 SQL connection:\n{conn}\n")

        #Create cursor object if connection is succesful
        if conn != None:
            cur = conn.cursor()
        #Now execute the above query we prepared
        cur.execute(sql_fetch_query)
        #And store the data from the cursor, to a variable.
        table_data = cur.fetchall()
        #Then itterate through the data using a for loop to print.
        for num, row in enumerate(table_data):
            print(f"row: {row}")
            print(type(row))
            print("\n")
        #Finally, be sure to close the connectiosn to avoid memory leaks(just in case)
        cur.close()
        conn.close()
    
        

        
    
    except psycopg2.Error as errErr:
        print("An error has occured...")
        psqle.print_psycopg2_exception(errErr)
        conn = None

    except psycopg2.OperationalError as errOp:
        print("An operational error has occured...")
        psqle.print_psycopg2_exception(errOp)
        conn = None

    except Exception as errExc:
        print("A general exception has occured...")
        psqle.print_psycopg2_exception(errExc)
        conn = None
    """
table_fetch()