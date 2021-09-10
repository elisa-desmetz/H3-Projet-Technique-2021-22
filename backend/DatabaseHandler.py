import os
from sqlalchemy import create_engine, Table, MetaData, select
import logging
from sqlalchemy.engine.base import Connection
import pymysql

config = {
    'user' : 'user',
    'password' : 'pass',
    'host' : 'db',
    'port' : 3306,
    'database' : 'database'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

connection_str = f'mysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
engine = create_engine(connection_str)
connection = engine.connect()
metadata = MetaData()

jobxpdata = Table('jobxpdata', metadata, autoload=True,autoload_with=engine)

def GetCraftByJobId(job_id):
    logging.info(jobxpdata.columns.keys())
    selection = select([jobxpdata]).where(jobxpdata.columns.job==job_id)
    return connection.execute(selection).fetchall()