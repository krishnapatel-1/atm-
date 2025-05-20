class Atm:
    def __init__(s ):
        s.__balance=0
        s.__pin='' 
       
    def menu(s):
        while(True):
         try:
            user=input(''' Hello , how would you proceed ?
                       Enter 1 to creat PIN 
                       Enter 2 to deposit 
                       Enter 3 to  check balance
                       Enter 4 withdraw cash
                       Enter 5 to Exit      ''')
            
         except Exception as  e:
              print('error is ',e)
         else:
            if user =='1':
             s.create_pin()
            elif user =='2':
             s.deposit()
            elif user=='3':
             s.check_balance()
            elif user=='4':
             s. withdraw()
            else :
             exit()
    def get_pin(s):
        print( 'pin is',s.__pin)
    def set_pin(s,new_pin):
        if new_pin==str:

         s.__pin=new_pin
         print ('pin changed successfully')

        else:
          print('not changed')
    def create_pin(s):

        p=input('Enter the new PIN')
        if p==s.__pin:
            print("PIN already exit ")
        else:
            s.__pin=p
            print('PIN successfully created ')
    def deposit(s):
         p=input('Enter PIN')
         if p==s.__pin:
            print("PIN Found ")
            s.__balance+=int(input('Enter the amount to be deposit '))
            print('deposit successful')
         else:
    
            print('invalid PIN ')
    def check_balance(s):
         p=input('Enter PIN')
         if p==s.__pin:
            print("Your balance is  ",s.__balance)
            
         else:
    
            print('invalid PIN ')
    def  withdraw(s):
        p=input('Enter PIN')
        if p==s.__pin:
            amount=int(input('Enter the amount to be withdraw'))
            if s.__balance >=amount:
                s.__balance-=amount
            else :
                print('insufficient balance ')
            print("Your balance is  ",s.__balance)
            
        else:
            
            print('invalid PIN ')
            

sbi=Atm()
sbi.set_pin(123)
sbi.get_pin()
sbi.menu()
   
 


    