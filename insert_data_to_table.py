import psycopg2
import os
from dotenv import load_dotenv
from psql_error_handler import print_psycopg2_exception as psqle
import re
import pyinputplus as pyip

# An effort to insert data into created table

# Load in login information
load_dotenv()
LOGIN_HOST = os.getenv('DB_HOST')
LOGIN_DBNAME = os.getenv('DB_NAME')
LOGIN_USER = os.getenv('DB_USER')
LOGIN_PASS = os.getenv('DB_PASS')
LOGIN_PORT = os.getenv('DB_PORT')
DB_CONNECTION_STRING = f"host={LOGIN_HOST} port={LOGIN_PORT} dbname={LOGIN_DBNAME} user={LOGIN_USER} password={LOGIN_PASS}"

# Establish the needed variables in global scope
TABLE_NAME = ""
GAME_TYPE = ""
GAME_DATE = ""
GAME_TIME = ""

def input_data():
    # Assemble the data requied through user input.
    # pyinputplus was useful to verify user input.
    TABLE_NAME = pyip.inputStr("Input table to update:\n", default="testtable",strip=None)
    GAME_TYPE = pyip.inputMenu(choices=["CPR","DND"],prompt="Which game should we play?\n", strip=None)
    GAME_DATE = pyip.inputDate("Enter the date of the session:\n",formats=["%Y/%m/%d"], strip=None)
    GAME_TIME = pyip.inputTime("Enter the time of the session:\n",formats=["%H:%M"],strip=None)
        #Create while loop to process confirmation of query.
    while True:
        inputCommit = pyip.inputChoice(["Y","N"],"\nPlease confirm query commit: Y/N?\n")
        if inputCommit == "Y":
            print(f"\nCommittin query...\n")
            print(f"\nProcessing query...\n")
            return insert_data(TABLE_NAME, GAME_TYPE, GAME_DATE,GAME_TIME)
        if inputCommit =="N":
            print(f"\nRolling back changes...\n")
            confirmQuit = pyip.inputChoice(["Y","N"],"\nDo you want to quit? Y/N\n")
            if confirmQuit == "Y":
                print("Goodbye!")
                break
            if confirmQuit == "N":
                return input_data()
    


def insert_data(TABLE_NAME, GAME_TYPE, GAME_DATE, GAME_TIME):
    # Process the data assembled to a SQL query, connect, send, and commit, then close.
    print("\nprocessing...\n")
        # SQL query format to send to postgreSQL server
    sql =   f"""  
            INSERT INTO {TABLE_NAME}(GAME_TYPE, GAME_DATE, GAME_TIME)
            VALUES('{GAME_TYPE}', '{GAME_DATE}', '{GAME_TIME}') RETURNING game_id;
            """
    try:
        # Open connection
        print(f"Connecting to {TABLE_NAME}, at {LOGIN_DBNAME}")
        conn = psycopg2.connect(DB_CONNECTION_STRING)
        print(f"Connection succesful, querying to {LOGIN_DBNAME}, {TABLE_NAME}")
        # Create cursor object
        cur = conn.cursor()
        # Execute established query
        cur.execute(sql)
        # Fetch new game ID
        print(f"Success! -- Fetching game ID...")
        game_id = cur.fetchone()[0]
        # Commit the whole thing
        conn.commit()
        # Print victory speech
        print("Success! -- The following game was added:")
        print(f"Game ID: {game_id}. {GAME_TYPE}, on the {GAME_DATE}, at {GAME_TIME}, has been added to {TABLE_NAME}")
    except(Exception, psycopg2.DatabaseError) as err:
        psqle(err)
    finally:
        if conn is not None:
            conn.close()
input_data()