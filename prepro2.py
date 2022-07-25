'''prepro2'''
def main():
    '''prepro ez'''
    money = int(input())
    money10 = money
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    money -= water
    if money % 3 == 0:
        money3 = snack1 * 10
        snacks1 = 10 * snack1
    elif money % 3 == 1:
        money3 = snack1 * 15
        snacks1 = 15 * snack1
    else:
        money3 = snack1 * 20
        snacks1 = 20 * snack1
    money -= money3
    snack5 = money % 3
    if snack5 == 0:
        money5 = snack2 * 12
        snacks2 = 12 * snack2
    elif money % 3 == 1:
        money5 = snack2 * 15
        snacks2 = 15 * snack2
    else:
        money5 = snack2 * 18
        snacks2 = 18 * snack2
    money -= money5
    snack6 = money % 3
    if snack6 == 0:
        money7 = snack3 * 5
        snacks3 = 5 * snack3
    elif snack6 == 1:
        money7 = snack3 * 7
        snacks3 = 7 * snack3
    else:
        money7 = snack3 * 9
        snacks3 = 9 * snack3
    money -= money7
    if money < 0:
        print("Now you have %d left." %money10)
        print("You don't have enough money!")
    else:
        print('Now you have %d left.' %money)
        print("Here's your order!")
        print('Water: %d baht' %water)
        print('Snack number 1: %d baht' %snacks1)
        print('Snack number 2: %d baht' %snacks2)
        print('Snack number 3: %d baht' %snacks3)
main()
