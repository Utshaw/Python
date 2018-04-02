


films = {
    'Finding Dory': [3, 5],
    'Boss Baby': [2, 5],
    'Despicable Me': [18, 5]
}


while True:

    choice  = input('What film would you like to watch? ').strip().title()

    if choice in films:
        age = int(input('Whats your age? ').strip())
        if age >= films[choice][1]:
            print('Go On!!!')
        else:
            print('You arent old enough to watch this.')
        pass
    else:
        print('We dont have that film right now!!')



