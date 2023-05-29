# Import python library sys for detailed exception information
import sys

# Import connect library from psycopg2
from psycopg2 import connect

# Import exception handlers from psycopg2
from psycopg2 import OperationalError, errorcodes, errors

# import __version__ attribute from psycopg2 for older adapters
from psycopg2 import __version__ as psycopg2_version

"""
=======================================
I made this module in an effort to 
streamline the troubleshooting and exception handling 
when developing and testing pythong > postgresql database handling
=======================================
"""



# Function that handles and parses a psycopg2 exception
def print_psycopg2_exception(err):
    print(f"An exception has occured, see below...")
    print(f"\npsycopg2 version: {psycopg2_version} \n")
    # Fetch details of exception, assign to various variables
    err_type, err_obj, traceback = sys.exc_info()
    # And line numbers for easy reference
    line_num = traceback.tb_lineno

    # Print connect() error
    print(f"\npsycopg2 ERROR: \n{err}on line number: {line_num}\n")
    print(f"psycopg2 traceback: \n{traceback} type: {err_type}")

    # Fetch and print psycopg2 extensions.Diagnostics object attribute
    print(f"\nextensions.diagnostics: {err.diag}")

    # Fetch and print pgcode and pgerror
    print(f"postgresSQL error: {err.pgerror}")
    print(f"postgresSQL code: {err.pgcode}\n")
