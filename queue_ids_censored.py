"""queue_ids.py

## **This is a Python script that extracts queue_id information from a JSON file found on the riot api documentation website**
"""
import pandas as pd
import pymysql
from sqlalchemy import create_engine
import json

#This code only needs to be run once

#Create sql table in RDS if it doesn't exist
def create_table(cursor):
  sql = ('''CREATE TABLE IF NOT EXISTS queue_id_info (
             queue_id int PRIMARY KEY,
              queue_name VARCHAR(50)
             )''')
  cursor.execute(sql)

def convert_json_to_df(df):
    json_file = open('lol_queues.json')
    lol_queues = json.load(json_file)

    for queue in lol_queues:
        queue_id = queue['queueId']
        queue_name = queue['description']

        df = df.append({'queue_id': queue_id, 'queue_name': queue_name}, ignore_index = True)

    json_file.close()
    return df


#Amazon RDS information
dbname = 'XXX'
user = 'XXX'
password = 'XXX'
host = 'XXX'
port = 3306

#create sqlalchemy engine
db_data = 'mysql+pymysql://'+user+':'+password+'@'+host+':'+str(port)+'/'+dbname
engine = create_engine(db_data)

#connect to database
db = pymysql.connect(user = user,  password = password, 
                      host = host, database = dbname, port = port)
cursor = db.cursor()

#create MySQL table if it has not been created
create_table(cursor)

#initialize & populate dataframe
df = pd.DataFrame(columns = ['queue_id', 'queue_name'])
df = convert_json_to_df(df)

#load to rds
df.to_sql('queue_id_info', engine, if_exists = 'append', index = False)