import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(host=os.getenv('HOST'), dbname="postgres", user="postgres",
                        password=os.getenv('PASSWORD'))

cur = conn.cursor()
print("Please type the last name of the employee or employees you are looking for?: ")
last_name = input()

cur.execute("CALL last_name_GET(%s);", (last_name))

num = cur.fetchall()
print(num)
conn.commit()
cur.close()
conn.close()