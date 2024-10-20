import verify_pin
import deposite
import withdraw

def atm():
    pin=1234
    amount=10000
    if verify_pin.verify_pin(pin):
        while True:
            print(" 1)Withdraw  2)Deposite  3)Check balance  4)Exit ")
            opt=input('Enter your option: ')
            if not opt.isdigit():
                print('Enter valid option: ')
                continue
            opt=int(opt)

            if opt == 1:
                amount=withdraw.withdraw(amount)
            elif opt == 2:
                amount=deposite.deposite(amount)
            elif opt == 3:
                print('Your available balance is: ',amount)
            elif opt == 4:
                print('Thank you for banking with us, visit again.')
                break
            else:
                print('Enter valid option: ')

atm()


