import random

cards = [6, 7, 8, 9, 10, 2, 3, 4, 11]
random.shuffle(cards)
score = 0  
score2 = 0  
hod = 0 
print('Приветствую вас в игру "21 очко".')
while True:
    hod += 1
    if hod % 2 != 0: #ход игрока
        print('Ваш ход. Хотите взять карту? y/n')
        otvet = input().lower()
        if otvet == 'y':
            card = cards.pop()
            if card == 6:
                score += 6
                print(f'Вы вытащили шестерку. Кол-во очков: {score}')
            elif card == 7:
                score += 7
                print(f'Вы вытащили семерку. Кол-во очков: {score}')
            elif card == 8:
                score += 8
                print(f'Вы вытащили восьмерку. Кол-во очков: {score}')
            elif card == 9:
                score += 9
                print(f'Вы вытащили девятку. Кол-во очков: {score}')
            elif card == 10:
                score += 10
                print(f'Вы вытащили десятку. Кол-во очков: {score}')
            elif card == 2:
                score += 2
                print(f'Вы вытащили Вальта (2). Кол-во очков: {score}')
            elif card == 3:
                score += 3
                print(f'Вы вытащили Даму (3). Кол-во очков: {score}')
            elif card == 4:
                score += 4
                print(f'Вы вытащили Короля (4). Кол-во очков: {score}')
            else:
                score += 11
                print(f'Вы вытащили Туза (11). Кол-во очков: {score}')
            
            if score > 21:
                print(f'К сожалению, вы проиграли! Ваш счёт: {score}')
                print('Компьютер выиграл!')
                break
            elif score == 21:
                print(f'Поздравляю! Вы набрали 21 очко и выиграли!')
                break

        elif otvet == 'n':
            print(f'Вы завершили ход. Ваш итоговый счёт: {score}')
            break
        else:
            print('Я же сказал, ответь y/n, а не то, что ты написал!')

    else:  #ход компьютера
        print("\nХод компьютера...")
        if score2 < 17:
            card = cards.pop()
            if card == 6:
                score2 += 6
                print(f'Компьютер вытащил шестерку. Счёт компьютера: {score2}')
            elif card == 7:
                score2 += 7
                print(f'Компьютер вытащил семерку. Счёт компьютера: {score2}')
            elif card == 8:
                score2 += 8
                print(f'Компьютер вытащил восьмерку. Счёт компьютера: {score2}')
            elif card == 9:
                score2 += 9
                print(f'Компьютер вытащил девятку. Счёт компьютера: {score2}')
            elif card == 10:
                score2 += 10
                print(f'Компьютер вытащил десятку. Счёт компьютера: {score2}')
            elif card == 2:
                score2 += 2
                print(f'Компьютер вытащил Вальта (2). Счёт компьютера: {score2}')
            elif card == 3:
                score2 += 3
                print(f'Компьютер вытащил Даму (3). Счёт компьютера: {score2}')
            elif card == 4:
                score2 += 4
                print(f'Компьютер вытащил Короля (4). Счёт компьютера: {score2}')
            else:
                score2 += 11
                print(f'Компьютер вытащил Туза (11). Счёт компьютера: {score2}')

            if score2 > 21:
                print(f'Компьютер проиграл! Его счёт: {score2}')
                print('Поздравляем! Вы выиграли!')
                break
            elif score2 == 21:
                print(f'Компьютер набрал 21 очко! Компьютер выиграл!')
                break
        else:
            print(f'Компьютер завершил ход. Итоговый счёт компьютера: {score2}')
            break
print("\n--- Конец игры ---")
print(f'Ваш итоговый счёт: {score}')
print(f'Счёт компьютера: {score2}')

if score <= 21 and (score > score2 or score2 > 21):
    print("Поздравляю! Вы победили!")
elif score2 <= 21 and (score2 > score or score > 21):
    print("Компьютер выиграл. Попробуйте ещё раз!")
else:
    print("Ничья!")
