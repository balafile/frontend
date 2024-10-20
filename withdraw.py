def withdraw(amount):
    inp=int(input('Enter a withdraw amount: '))
    if inp > amount:
        print('Insufficient balance. ')
    else:
        amount -= inp
        print('Withdraw amount is: ',inp)
        print('Your current balance is: ',amount)
    return amount