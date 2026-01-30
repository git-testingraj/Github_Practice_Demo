'''var = eval(input("Please enter the value: "))
for i in range(var+1):
    if i%2 == 0:
        print(i)
    else:
        pass'''

import pandas as pd
import pyodbc
import oracledb
import logging
from sqlalchemy import create_engine

oracledb.init_oracle_client(lib_dir=r"C:\oraclexe\app\oracle\instantclient_19_29")

#MSSQL DB Connection
db_connection = ("mssql+pyodbc://LAPTOP-R3E5KI54\SQLEXPRESS/ETL_Auto_Practice?"
                 "driver=ODBC+Driver+17+for+SQL+Server")
eng_conn = create_engine(db_connection)

#ORACLE DB Connection
oracle_connection = create_engine("oracle+oraclecb://ETL_Automation:ETL_Automation@localhost:1521/xe")