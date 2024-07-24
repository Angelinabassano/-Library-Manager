from dotenv import load_dotenv
import psycopg2
import os


load_dotenv()

connection = psycopg2.connect(host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'), user=os.getenv('DB_USER'),
                                              password=os.getenv('DB_PASSWORD'), database=os.getenv('DB_NAMEDB'))

print(connection)
