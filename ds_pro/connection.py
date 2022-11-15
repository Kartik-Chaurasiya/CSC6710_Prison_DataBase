import psycopg2

conn = psycopg2.connect(
    database="dbms", user='postgres', password='123456', host='127.0.0.1', port= '5432'
    )
