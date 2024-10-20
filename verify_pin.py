def verify_pin(pin):
    while True:
        inpin=int(input("Enter pin no: "))
        if inpin == pin:
            print("Welcome to ABC Bank")
            return True
        else:
            print('Enter valid pin: ')