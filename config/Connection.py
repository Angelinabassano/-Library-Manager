import psycopg2

connection = psycopg2.connect(
    host='127.0.0.1',
    port='5432',
    user='postgres',
    password='1234ab',
    database='Library_Manager'
)

print(connection)