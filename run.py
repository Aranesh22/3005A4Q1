import psycopg2 

hostname = 'localhost' 
database = 'student' 
username = 'postgres' 
pwd = 'Vignesh8*' 
port_id = 5433  
conn = None 
cur = None

try:
    conn = psycopg2.connect ( 

        host = hostname, 
        dbname = database, 
        user = username, 
        password = pwd, 
        port = port_id) 

    cur = conn.cursor()

    """
    script = ''' INSERT INTO students (first_name, last_name, email, enrollment_date) Values (%s,%s,%s,%s)
                
    '''   
    
    insertVal = ('aran','van','rat@jack.com','2023-09-20')
    cur.execute(script,insertVal)
    conn.commit()   
    """

    """
    cur.execute('SELECT * FROM STUDENTS') 
    for x in cur.fetchall(): 
        print(x)   

    conn.commit()    
     """  
    
    """
    update_script = 'UPDATE students SET email =%s WHERE student_id = %s' 
    val = ('a.aranesh@gmail.com',5) 
    cur.execute(update_script,val) 
    conn.commit() 
    """  

    """
    delete_script = 'DELETE FROM students WHERE student_id =%s'  
    val= '5' 
    cur.execute(delete_script,val) 
    conn.commit() 
    """
    
    val = ""
    
    while (val!=0):   
        val = input("Enter 1 - for add user \n Enter 2 -to delete user\n Enter 3 to read DB\n Enter 4 to update email\n") 
        if val == "1":  

            #conn.commit()  
            print("Thank youuuuuuuuuuuuuuuuuuuuuuu") 
            enterUserData()
        
        elif val == "2":  
            #conn.commit()  
            print("Thank youuuuuuuuuuuuuuuuuuuuuuu")

        elif val == "3": 
            #conn.commit()    
            print("Thank youuuuuuuuuuuuuuuuuuuuuuu")
        
        elif val == "4": 
            #conn.commit()    
            print("Thank youuuuuuuuuuuuuuuuuuuuuuu")
        
        elif val == "5":  
            print("Thank youuuuuuuuuuuuuuuuuuuuuuu")
            break 
        else:  
            print("try again")
           
        


    

except Exception as error: 
    print(error) 
finally:  

    if cur is not None:
        cur.close() 
    if conn is not None: 
        conn.close()
    cur.close() 
    conn.close() 

def enterUserData(): 
    val = input("Enter user first name");
