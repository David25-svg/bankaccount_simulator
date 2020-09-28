"""
this project is simulating someone's bank account.
Starts by obtaining the customer's name and pin number (use: 0000 for correct pin number).
the program Allow the customer to exit when choosing a transaction or after.
If the pin number is correct, the program ask if he/she wants to deposit or withdraw from their account.
theres is a Starting amount with $1,000.00 in the account as a balance. If the transaction is a deposit,
the program adds to previous balance and display the new balance.
If it is a withdrawal, the program calculate and also display the account balance.
Each time, the program ask if they want to perform another transaction, and exits if they choose 'no'.
If the pin number is incorrect, the prgram exit.
"""
Fullname= input('Enter Full Name:')#asking the user to input Full Name 
ssnumber= int(input('enter social security number:'))#asking the user to input social security number
pin= int(input('Enter 4 digit pin:'))#asking the user to input pin number
if pin==0000:#(use: 0000 for correct pin number)
    action=input('Would you like to make a deposit or withdraw? ,d for depossit,w for withdraw:')
    #^^asking user if they would like to make a deposit or withdraw^^
    if action=='d':#if user wants to make deposit
        #Start with $1,000.00 in the account as a balance.
        print (Fullname,'your account Balance is: ',1000 )#displaying original set balance
        al=int(input('enter the amout you would like to Deposit:'))#asking user to imput amout to deposite
        newbal= (al+1000)#formula for adding the deposited amonut to the set amount that was already in the bank
        print (Fullname,'your new balance is:',newbal,)#new balance after diposit
    else:#if user wants to make withdrawl
        print (Fullname,'your account Balance is ',1000 )#Start with $1,000.00 in the account as a balance.
        wi=int(input('enter the amout you would like to withdraw:'))#asking the user the widral amount
        newamount= (1000-wi)#formula fo subtrating the withdral amout from the original amount 
        print (Fullname,'your new balance is: ',newamount,)#new balance after withdral  
else:
    exit
    
oncemore= input('would you like To preform another transaction ,y for yes,n for no:')#
if oncemore=='y':
    Fullname= input('Enter Full Name:')#asking the user to input Full Name 
    ssnumber= int(input('enter social security number:'))#asking the user to input social security number
    pin= int(input('Enter 4 digit pin:'))#asking the user to input pin number
    action=input('Would you like to make a deposit or withdraw? ,d for depossit,w for withdraw:')
    #^^asking user if they would like to make a deposit or withdraw^^
    if action=='d':#if user wants to make deposit
        print (Fullname,'your new balance is: ',1000 )#displaying original set balance
        al=int(input('enter the amout you would like to Deposit:'))#asking user to imput amout to deposite
        newbal= (al+1000)#formula for adding the deposited amonut to the set amount that was already in the bank
        print (Fullname,'your new balance is:',newbal)#new balance after diposit
    else:#if user wants to make withdrawl
        print (Fullname,'your account Balance is: ',1000)#displaying original set balance
        wi=int(input('enter the amout you would like to withdraw:'))#asking the user the widral amount
        newamount= (1000-wi)#formula fo subtrating the withdral amout from the original amount
        print (Fullname,'your new balance is',newamount,)#new balance after withdral    

