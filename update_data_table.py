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
    TABLE_NAME = pyip.inputStr("\nInput table to update:\n", default="testtable",strip=None)
    game_id = pyip.inputNum("\nPlease input the game session id to update:\n")
    GAME_TYPE = pyip.inputMenu(choices=["CPR","DND"],prompt="\nChange game played to:\n", strip=None)
    GAME_DATE = pyip.inputDate("\nEnter the date of the session:\n",formats=["%Y/%m/%d"], strip=None)
    GAME_TIME = pyip.inputTime("\nEnter the time of the session:\n",formats=["%H:%M"],strip=None)
    #Create while loop to process confirmation of query.
    while True:
        inputCommit = pyip.inputChoice(["Y","N"],"\nPlease confirm query commit: Y/N?\n")
        if inputCommit == "Y"
            print(f"\nCommittin query...\n")
            return update_data(game_id,TABLE_NAME, GAME_TYPE, GAME_DATE,GAME_TIME)
        if inputCommit =="N":
            print(f"\nRolling back changes...\n")
            confirmQuit = pyip.inputChoice(["Y","N"],"\nDo you want to quit? Y/N\n")
            if confirmQuit == "Y":
                print("Goodbye!")
                break
            if confirmQuit == "N":
                return input_data()

#If confirmed, query is sent to update_data
def update_data(game_id,TABLE_NAME, GAME_TYPE,GAME_DATE,GAME_TIME):
    #query here
    update_sql = f"""UPDATE {TABLE_NAME} 
    SET game_type='{GAME_TYPE}',
    game_date='{GAME_DATE}',
    game_time='{GAME_TIME}'
    WHERE game_id='{game_id}'
    RETURNING game_id;
    """

    conn = None
    updated_rows = 0
    #Establish connection and commit changes.
    try:
        print(f"\nConnecting to: {LOGIN_DBNAME}\n")
        conn = psycopg2.connect(DB_CONNECTION_STRING)
        print(f"\nSetting up query...\n")
        cur = conn.cursor()
        print(f"Sending query to game session id: {game_id}")
        cur.execute(update_sql)
        updated_rows = cur.rowcount
        conn.commit()        
        print(f"Success! Game session ID: {game_id} has been updated!")
        print("\nClosing connection... goodbye!")
        cur.close()
    except(Exception, psycopg2.DatabaseError) as Err:
        psqle(Err)
    return(updated_rows)
input_data()