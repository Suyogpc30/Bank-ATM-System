db={10101:{'name':'suyog','city':'nashik','pin':9834,'balance':20000,'m_n':9834163754,'act':'crurrent'},102:{'name':'pravin','city':'nashik','pin':9767,'balance':10000,'m_n':9767196869,'act':'saving'},103:{'name':'pradip','city':'nashik','pin':8554,'balance':30000,'m_n':8554956442,'act':'current'},104:{'name':'pranav','city':'jalgaon','pin':7066,'balance':25000,'m_n':7066792992,'act':'saving'},105:{'name':'darshan','city':'nashik','pin':7218,'balance':20000000,'m_n':7218282628,'act':'credit'}}

ac=int(input('Enter a card number:'))
if ac in db:
    pin=int(input('Enter a pin: '))
    if pin==db[ac]['pin']:
        print('-'*130)
        print(' '*42,'Hello',db[ac]['name'])
        print("""
                                    ---------------------------                                  
                                    |  Welcome To AAJAO BANK  |                 
                                    |-------------------------|                                  
                                    |  1.Withdraw money       |          
                                    |  2.Check balance        |            
                                    |  3.Deposite balance     |               
                                    |  4.Update pin           |                     
                                    |  5.Check your detail    |     
                                    |                         |   
                                    ---------------------------               
        """)
        print('-'*130)

        ch=int(input('Enter your choise: '))
        if ch==1:
            am=int(input('Enter a amount:'))
            if am<db[ac]['balance']:
                db[ac]['balance']=db[ac]['balance']-am
                print('your money withdraw successfuly')
                print(db[ac]['name'],'Available balance is:',db[ac]['balance'])
            else:
                print('Balance is Insufficient')
        elif ch==2:
            print('Available balance is:',db[ac]['balance'])
        elif ch==3:
            am=int(input('Enter a amount:'))
            db[ac]['balance']=db[ac]['balance']+am
            print('Your Money is Deosited Successfully')
            print(db[ac]['name'],'Balance is:',db[ac]['balance'])
        elif ch==4:
            op=int(input('Enter a old pin:'))
            if op==db[ac]['pin']:
                np=int(input('Enter a new pin:'))
                db[ac]['pin']=np
                print('Your Pin Will be Updated')
        elif ch==5:
            print('-'*85)
            print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format('name','city','phone no.','Balance'))
            print('-'*85)

            for i in db:
                if ac in db:
                    print('-'*85)
                    print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format(db[ac]['name'],db[ac]['city'],db[ac]['m_n'],db[ac]['balance']))
                    print('-'*85)
                    break
        else:
            print('Invalid input')
    
    else:
        print('Invalid pin')

else:
    print('Invalid card number')