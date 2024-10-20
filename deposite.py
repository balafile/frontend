def deposite(amount):
    ent=int(input('Enter deposit amount: '))
    if ent <= 0:
        print('Enter valid deposite amount: ')
    else:
        amount += ent
        print('Tour deposited amount is: ',ent)
    return amount