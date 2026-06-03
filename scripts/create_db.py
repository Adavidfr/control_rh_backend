import psycopg2
from psycopg2 import sql

DB = {
    'host': 'localhost',
    'port': 5433,
    'user': 'postgres',
    'password': 'postgres',
}

dbname = 'control_rh'

try:
    conn = psycopg2.connect(dbname='postgres', options='-c client_encoding=UTF8', **DB)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql.SQL('CREATE DATABASE {}').format(sql.Identifier(dbname)))
    print('Database created:', dbname)
    cur.close()
    conn.close()
except Exception as e:
    print('Error creating database:', e)
