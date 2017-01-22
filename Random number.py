from random import *
print( "\t\t\tДобро пожаловать в игру 'Отгадай число'!")
print("\n\t\tЯ загадал натуральное число из диапазона от 1 до 100.")
print("\n\t\tПостарайтесь отгадать его за 7 попыток.\n")
the_number = randint(1, 100)
guess = int(input("Baшe предположение: "))
tries = 1
while guess != the_number :
    if guess > the_number:
        print( "Меньше...")
    else:
        print( "Больше...")
    guess = int ( input ("Ваше предположение: "))
    tries += 1
    if guess == the_number:
        print("\n\t\tBaм удалось отгадать число! Это и в самом деле", the_number)
        print("\n\t\tBы затратили на отгадывание всего лишь ", tries, " попыток!\n")
        break
    if tries==7 :
        print('Вы проиграли')
        break
input('\n\t\tНажмите Enter для завершения ! ')
