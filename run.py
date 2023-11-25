import psycopg2 

#connection dependenices needed to make the connection
hostname = 'localhost' 
database = 'student' 
username = 'postgres' 
pwd = 'Vignesh8*' 
port_id = 5433  
conn = None 
cur = None 

'''
This is the main function responsible for making the connection with the database
it also runs as the function that communicated with the database and in charge of the user experience 
A while loop is used to cycle through the interface for the user choices and make commands to sql databse and update the DB
'''
def main(): 

    #try statment is used to make the connection 
    try:
        conn = psycopg2.connect ( 

            host = hostname, 
            dbname = database, 
            user = username, 
            password = pwd, 
            port = port_id) 

        #This statment allows us to connect towards SQL in order to execute those commands
        cur = conn.cursor()

        val = ""
        
        #Using this while loop to cycle through the interface 
        while (val!=5):   
            val = input("\nEnter 1 - for add user \nEnter 2 -to delete user\nEnter 3 to read DB\nEnter 4 to update email\nEnter 5 to exit\n") 
            if val == "1":  

                userin = enterUserData() 

                query = ' INSERT INTO students (first_name, last_name, email, enrollment_date) Values (%s,%s,%s,%s) '  
                cur.execute(query,userin) 
                conn.commit() 
                print("User added \n")

            elif val == "2":   
                delete_script = 'DELETE FROM students WHERE student_id =%s' 
                userDelId = deleteUser()  
                cur.execute(delete_script,userDelId) 
                conn.commit()  
                print("User Deleted\n")

            elif val == "3": 
              
                cur.execute('SELECT * FROM STUDENTS ORDER By Student_id ASC')  
                for x in cur.fetchall(): 
                    print(x)  
                   
                conn.commit() 
               
            
            elif val == "4": 
               

                valid = True
                while (valid!=False):    
                    contentE = updateEmail() 
                    test = 'SELECT student_id FROM students WHERE student_id= %s'  
                    inP = contentE[0] 
                    print(str(inP))
                    cur.execute(test,str(inP))  
                    lent = len(cur.fetchall())   
                    conn.commit()  
                   
                    print(lent)

                    if (int(lent) == 0):  
                         print("ID DOEST NOT EXIST TRY AGAIN")      
                    else:  

                        val = contentE[1]  
                        test = "SELECT email FROM students WHERE email =%s" 

                        cur.execute(test,(val,))  
                        conn.commit()   

                        if not cur.fetchall():  
                            update_script = 'UPDATE students SET email =%s WHERE student_id = %s'   
                            userin = (contentE[1],contentE[0])
                            cur.execute(update_script,userin) 
                            conn.commit() 
                            print("\nUSER UPDATED!\n")
                            break       
                        else: 
                            print("EMAIL IS ALREADY IN DATABASE PLEASE TRY AGAIN!") 
            
            elif val == "5":  
                break 
            else:  
                print("try again")

    except Exception as error: 
        print(error)  
    #Finally is used to close the connection
    finally:  
        if cur is not None:
            cur.close() 
        if conn is not None: 
            conn.close()
        cur.close() 
        conn.close() 

''' 
This function is used for receving 
the deletuser input is then checked if they are valid inputs   
''' 

def deleteUser():   
     userInput = ""    
     valid = True;   
     id = 0 


     while (userInput!="exit"):    

        while (valid!=False): 
               userInput = input("Enter user ID \n") 

               if (checkifNum(userInput) == True):  
                   
                   id = userInput 
                   userInput= ""  
                   break
               else:  
                   print("Must be a number")  
        
        return id
     

''' 
This function checks if the a string contains a number 
'''
def checkifNum(val): 
     for x in val: 
          if x.isdigit(): 
               return True 
          
          
     return False

''' 
This function is like the other functions where it recieves the userinput 
and checks if its valid based on the premises 
'''
def updateEmail():    
     
    userInput = ""   
    id = 0 
    email = ""
    valid = True 
    contentEmail = "" 
    id = 0

    while (userInput!="exit"):    

        while (valid!=False): 
               userInput = input("Enter user ID \n") 

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
     
''' 
This function takes in all the user data for add user as well as doing error checking and sending the data back to the main function 
'''     
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

               if (checkifNum(userInput) == True) and (len(userInput) ==1 or len(userInput) ==2) and 0 < int(userInput ) < 13: 
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