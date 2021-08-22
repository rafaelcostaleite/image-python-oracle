#pip install cx_Oracle --upgrade

import pandas as pd
import cx_Oracle
import sys
import logging

#cx_Oracle.init_oracle_client(lib_dir=config['oracle']['lib_dir'])

connection = cx_Oracle.connect(
    user="totvs",
    password="",
    dsn="10.3.0.105:1245/JASPE")

df_ora = pd.read_sql("select A1_COD from SA1000 WHERE A1_COD < '0001000' ", con=connection)

connection.close()

print(df_ora.info())
