import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(host=os.getenv('HOST'), dbname="postgres", user="postgres",
                        password=os.getenv('PASSWORD'))

cur = conn.cursor()

cur.execute(""" 
    select count(id) from employees;
""")
print(cur.fetchone())
conn.commit()
cur.close()
conn.close()