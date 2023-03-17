from sass import balance 
print("~~welcome~~")
print("---SBI ATM---")
print("1> cash deposit", "\n2> cash withdrawal","\n 3> check balance")
user1 = input("Select Option")
pin = int(input("Enter Pin"))
if pin != 1111:
        print("Wrong Pin Entered Try Again")

if   user1 == "cash withdrawal" and pin == 1111:
    withdraw = int(input("Enter Amount"))
    balance = balance - withdraw
    print("Your Updated Balance :", balance)
    g = open("sass.py","w")
    balance = "balance"+"="+ str(balance)
    g.write(balance)
    user = input("DO YOU WANT A RECEIPE ?")
    
    if user == "yes":
        print (f'''YOUR  TRANSACTION RECEIPE
        DATE      TIME     ATM ID)
        XXX       XXXX     ACRO1112222
        CARD NO : 324XXXXXXX5608
        RECORD NO : XXXX
        AMT DEBITED TO YOUR ACCOUNT : {withdraw}
        AVAILABLE BALANCE : {balance}
        ''')
    else : print("Thankyou For Using Atm")    
elif   user1 == "cash deposit" and pin == 1111:
    add = int(input("Insert Cash Amount"))
    balance = balance+add
    print(" Your Updated Balance",balance)
    h = open("sass.py","w")
    balance = "balance"+ "=" + str(balance)
    h.write(balance)
    user = input("DO YOU WANT A RECEIPE ?")
    if user == "yes":
        print(f'''YOUR TRANSACTION RECEIPE
        DATE   TIME    AMT ID
        XXX    XXXX    ACRO1112222
        CARD NO : 324XXXXXXX5608
        RECORD NO : XXXX
        AMT CREDITED TO YOUR ACCOUNT: {add}
        AVAILABLE BALANCE : {balance}
        ''')
    else : print("Thankyou For Using Atm") 
elif user1 == "check balance" and pin ==1111:
    print("AVAILABLE BALANCE IN YOUR ACCOUNT :",balance)       
elif balance == 0 or pin == 1111:
      print("insufficent balance")
           
      
        

    


