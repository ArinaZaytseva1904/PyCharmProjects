from random import *
print('Хотите сыграть в игру "Отгадай слово"? "Да или нет?"- вот главный вопрос.')
for i in range(0, 100):
    a = sample('АЕНОСТ', 4)
    a = str(a)
    a = a.replace(',', '')
    a = a.replace(' ', '')
    a = a.replace('[', '')
    a = a.replace(']', '')
    a = a.replace("'", '')
    counter = 1
    otvet = ''
    print(a)
    answer = input('')
    answer = answer.title()
    if answer == 'Да':
        print('Отлично, тогда начнем.Отгадайте слово, составленное из букв: А, Е, Н, О, С, Т.У вас 10 попыток, удачи.')
        while counter != 11:
            prav = 0
            neprav = 0
            print('Попытка №', counter)
            counter += 1
            print('Впишите свой ответ:')
            otvet = input('')
            otvet = otvet.upper()
            if len(otvet) != 4:
                print('Букв должно быть 4, исправьтесь')
                otvet = input('')
            else:
                otvet = otvet
            if otvet == a:
                counter = 11
                print('Букв на своем месте: 4')
                print('Букв на чужом месте: 0')
                print('Вы выиграли! Поздравляю! Хотите попытать удачу вновь?')
            elif otvet != a:
                if a[0] == otvet[0]:
                    prav += 1
                elif a[0] != otvet[0]:
                    neprav += 1
                if a[1] == otvet[1]:
                    prav += 1
                elif a[1] != otvet[1]:
                    neprav += 1
                if a[2] == otvet[2]:
                    prav += 1
                elif a[2] != otvet[2]:
                    neprav += 1
                if a[3] == otvet[3]:
                    prav += 1
                elif a[3] != otvet[3]:
                    neprav += 1
                print('Букв на своем месте:', prav)
                print('Букв не на своем месте: ', neprav)
            if counter == 11 and a != otvet:
                print('Извините, но вы проиграли. Хотите попробовать снова?')
    elif answer == 'Нет':
        print('Ну ничего, поиграем в другой раз. ')
        break

