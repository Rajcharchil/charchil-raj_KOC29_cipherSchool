print("Welcome to Raj Bank ")
pin = 5555
chances = 3
balance = 5000
while chances != 0:                                                 ##while loop that executes a specified statement until the test condition evaluates to false

 
    user_pin = int(input("please enter the four digit pin :"))
    if user_pin != pin:
        chances -= 1                                                 ## if you  enter wrong pin then your chance will reduce by 1
        print("worng pin number ")                                     ##  you enter right pin then move Else condition  
        print(f"you have {chances} chances left")                      ## 'f' is use for formate purpose {} 

    
       
    else:                                                                      
        user_choice = input("B : Balance, D : Deposit, W : Withdraw :=  ")


        if user_choice == "B":
            print(f"Mr.Jhon , Available  balance in your account is Rs.{balance}")               

        if user_choice == "D":
            deposit_user = int(input("enter the amount that you would like to deposite : "))
            total_balance = deposit_user + balance
            print(f"you have deposited Rs.{deposit_user}")  
            print(f"your total balance is Rs.{total_balance} ")

        if user_choice == "W":
            withdraw_user = int(input("Enter the amount you want to withdraw : "))
            total_balance = balance - withdraw_user
            print(f"you have widhdrawn Rs.{withdraw_user}")
            print(f"your total balance is Rs.{total_balance}")


    user_exit = input("would you like to exit? yes/no :=")        ##new condition :- if user enter yes than loop is break with have a nice day. exit
    if user_exit == "yes":                                                            
        print('''
                        
                         thankyou for using Raj bank ! ! 
               
  _    _                                                                        _                                         
 | |  | |                                            (_)                     | |                  
 | |__| |   __ _  __   __   ___      __ _     _ __    _    ___    ___      __| |   __ _   _   _   
 |  __  |  / _` | \ \ / /  / _ \    / _` |   | '_ \  | |  / __|  / _ \    / _` |  / _` | | | | |  
 | |  | | | (_| |  \ V /  |  __/   | (_| |   | | | | | | | (__  |  __/   | (_| | | (_| | | |_| |  
 |_|  |_|  \__,_|   \_/    \___|    \__,_|   |_| |_| |_|  \___|  \___|    \__,_|  \__,_|  \__, |  
                                                                                           __/ |  
                                                                                          |___/ ''')
        
   
        break                ##the break statement we can stop the loop even if the while condition is true
    else:
        continue                 





                             ##while loop = yeh pehle condition ko check karta hain or fir instruction deta hain .loop code ko jab tak execute kare jab tak condation false na aa jaye 
                                             
                                            

''' f = it is a way to format your string that is more readable and fast. 
The f or F in front of strings tell Python to look at the values inside {} and
 substitute them with the variables values if exists'''
