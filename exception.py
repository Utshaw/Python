

def divideByNum(num):
    try:
        return 42 / num
    except ZeroDivisionError:
        print('Attempt for dividing ny zero.')




print(divideByNum(21))

print(divideByNum(0))




print('This is some')


def numCats(num):
    try:
        if num >= 4:
            print('You have a lot of cats!!')
        else:
            print('That is not that many cats')
    except TypeError:
        print('You did\'t enter a number')



numCats(100)

numCats('hundred')

