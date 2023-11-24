import psycopg2 

hostname = 'localhost' 
database = 'student' 
username = 'postgres' 
pwd = 'Vignesh8*' 
port_id = 5433  
conn = None 
cur = None   
def main():
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
        
        while (val!=5):   
            val = input("Enter 1 - for add user \n Enter 2 -to delete user\n Enter 3 to read DB\n Enter 4 to update email\n") 
            if val == "1":  

                #conn.commit()  
                print("Thank youuuuuuuuuuuuuuuuuuuuuuu") 
                userin = enterUserData() 

                query = ' INSERT INTO students (first_name, last_name, email, enrollment_date) Values (%s,%s,%s,%s) '  
                print(enterUserData)
                cur.execute(query,userin) 
                print("works")
                conn.commit()
           
            
            elif val == "2":   
                deleteUser()
                #conn.commit()  
                print("Thank youuuuuuuuuuuuuuuuuuuuuuu")

            elif val == "3": 
                #conn.commit()    
                print("Thank youuuuuuuuuuuuuuuuuuuuuuu") 
                """
                cur.execute('SELECT * FROM STUDENTS') 
                for x in cur.fetchall(): 
                    print(x)   

                conn.commit()    
               """  
            
            elif val == "4": 
                #conn.commit()  
                updateEmail()
                
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

def deleteUser():   
     userInput = ""    
     valid = True; 
     while (userInput!="exit"):    

        id = 0 

        while (valid!=False): 
               userInput = input("Enter user ID") 

               if (checkifNum(userInput) == True):  
                   
                   id = userInput
                   userInput= "" 
                   break
               else:  
                   print("Must be a number")  
        
        return id
     

def checkifNum(val): 
     for x in val: 
          if x.isdigit(): 
               return True 
          
          
     return False
    

def updateEmail():    
     
    userInput = ""   
    id = 0 
    email = ""
    valid = True 
    contentEmail = ""

    while (userInput!="exit"):    

        id = 0 

        while (valid!=False): 
               userInput = input("Enter user ID") 

               if (checkifNum(userInput) == True):  
                   
                   id = userInput
                   userInput= "" 
                   break
               else:  
                   print("Must be a number") 
        
        while (valid!=False): 
               userInput = input("Enter user email \n") 

               if userInput.__contains__("@") and userInput[0] !="@": 
                   email = userInput 
                   contentEmail = (id,email) 
                   userInput = "" 
                   break
               else:  
                   print("Invalid Email")
           
        
        return contentEmail
     
     
     
def enterUserData():    
    

    userInput = "" 
    valid = True  

    userInfo = "" 
    


    while (userInput!="exit"):    

        first_name= ""
        last_name = ""
        email = "" 
        year = 0
        month = 0
        day = 0
        
    

 
        while (valid!=False): 
               userInput = input("Enter user first name \n") 

               if (checkifNum(userInput) == True):  
                   print("dsa")
                   print("Name cant contain numbers!")  
                   userInput= ""
               else:  
                   first_name = userInput 
                   userInput = "" 

                   break 
        #valid = True  

        while (valid!=False): 
               userInput = input("Enter user last name \n") 

               if (checkifNum(userInput) == True): 
                   print("Name cant contain numbers!") 
               else:  
                   last_name = userInput 
                   userInput = "" 
                   break 
        
        while (valid!=False): 
               userInput = input("Enter user email \n") 

               if userInput.__contains__("@") and userInput[0] !="@": 
                   email = userInput 
                   userInput = "" 
                   break
               else:  
                   print("Invalid Email") 
        
        while (valid!=False): 
               userInput = input("Enter year of enrollment\n")  
               print(len(userInput))

               if  (checkifNum(userInput) == True)  and (len(userInput) ==4) and int(userInput) > 1799: 
                   year = (userInput)  
                   userInput = ""  
                   break

               else:   
                   print("Invalid input try again")  
        
        while (valid!=False): 
               userInput = input("Enter month of enrollment\n") 

               if (checkifNum(userInput) == True) and (len(userInput) ==1 or len(userInput) ==2) and int(userInput )> 0: 
                   month = userInput  
                   str(month)
                   userInput = "" 
                   break
               else:  
                   print("Invalid input try again")  
        
        while (valid!=False): 
               userInput = input("Enter day of enrollment\n") 

               if (checkifNum(userInput) == True) and (len(userInput) ==1 or len(userInput) ==2) and 0 < int(userInput) < 32: 
                   day = userInput    
                   date = year+"-"+month+"-"+day
                   userInfo = (first_name,last_name,email,date) 
                   print(userInfo)
                   userInput = "exit" 
                   break
               else:  
                   print("Invalid input try again")  

        return userInfo 
         
     



             
             
main()

                   
              
   

