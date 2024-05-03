#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
class BalancedExceptionError(Exception):
    pass
class AttemptedExceptionError(Exception):
    pass
attempts=1
def withdraw():
    saved_pin=1234
    
    global attempts
    balance=10000
    pin=int(input("Enter pin number:"))
    if saved_pin==pin:
        try:
            amt=float(input("Enter amount:"))
            temp_bal=balance-amt
            if temp_bal<1000:
                raise BalancedExceptionError('insufficent balance')
            print('Remaining balance is : ' ,temp_bal)
            
        except BalancedExceptionError as var:
            print(var)
    else:
        ans=input("Do you want to continue:(y/n):")
        if ans.lower()=='y':
            
            attempts=attempts+1
            print(attempts)
            try:
                if attempts==4:
                    raise AttemptedExceptionError('Wrong pin,Too many attempts your account locked for 1 hours')
                
            except AttemptedExceptionError as var1:
                
                print(var1)
                time.sleep(3600)
            else:
                 withdraw()
                
                   
        else:
            print('thank u')
            return
           
            
withdraw()            


# In[ ]:




