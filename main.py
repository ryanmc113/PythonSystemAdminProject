import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    # Establish a connection
    conn = psycopg2.connect(
                            host=os.getenv('HOST'), 
                            dbname="postgres", 
                            user="postgres",
                            password=os.getenv('PASSWORD'))
    
    cur = conn.cursor()
    print("Please type the last name of the employee or employees you are looking for?: ")
    last_name = "%" + input() + "%"
    #
    # cur.callproc('public.last_name_GET', (last_name))
    print(type(last_name))
    cur.execute("select * from find_last_names(%s);", (last_name,))

    names = cur.fetchall()
    print(names)
except psycopg2.Error as e:
    print(e)
finally:
    conn.commit()
    cur.close()
    conn.close()