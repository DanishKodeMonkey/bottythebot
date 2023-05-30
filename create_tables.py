import psycopg2
from dotenv import load_dotenv
import os
import psql_error_handler as psqle

load_dotenv()
#Create libpq connection string from env.
LOGIN_HOST = os.getenv('DB_HOST')
LOGIN_DBNAME = os.getenv('DB_NAME')
LOGIN_USER = os.getenv('DB_USER')
LOGIN_PASS = os.getenv('DB_PASS')
LOGIN_PORT = os.getenv('DB_PORT')
db_login = f"host={LOGIN_HOST} port={LOGIN_PORT} dbname={LOGIN_DBNAME} user={LOGIN_USER} password={LOGIN_PASS}"


def create_table(TABLE_NAME="testtable") -> bool:
   
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
    game_id SERIAL PRIMARY KEY,
    game_type VARCHAR(255) NOT NULL,
    game_date DATE NOT NULL,
    game_time TIME NOT NULL);
    """
    conn = None 
    try:
        #Connect to database
        print('connecting to postgreSQL database...')
        with psycopg2.connect(db_login) as conn:
            with conn.cursor() as cur:
                #Create tables in the postgreSQL database
                print('Creating new table...')
                cur.execute(create_table_sql)
            print('Table created succesfully... disconnecting')
            return True


    except psycopg2.Error as errErr:
        print("An error has occured...")
        psqle.print_psycopg2_exception(errErr)

    except psycopg2.OperationalError as errOp:
        print("An operational error has occured...")
        psqle.print_psycopg2_exception(errOp)
        
    except Exception as errExc:
        print("A general exception has occured...")
        psqle.print_psycopg2_exception(errExc)
    finally:
        cur.close()
        
create_table()
