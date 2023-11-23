import psycopg2 

hostname = 'localhost' 
database = 'student' 
username = 'postgres' 
pwd = 'Vignesh8*' 
port_id = 5433 

try:
    conn = psycopg2.connect ( 

    host = hostname, 
    dbname = database, 
    user = username, 
    password = pwd, 
    port = port_id)

    conn.close()

except Exception as error: 
    print(error)