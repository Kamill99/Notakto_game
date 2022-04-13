from random import randint as r

# Plansza do gry
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']

# Kombinacje, które kończą grę
defeat = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

# Wyświetlenie planszy z indeksami aby gracz się z nimi zapoznał
print()
print("        [0][1][2]")
print("        [3][4][5]")
print("        [6][7][8]")
print()
print("Oto plansza do gry, zapoznaj się z numerami indeksów")
print("Modyfikacja gry - kółko i krzyżyk")
print("Wstawiamy jedynie symbol X")
print("Przegrywa ten, kto postawi trzeci symbol w jednej linii")
print()

# Możliwości ruchu
possible_moves = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def easy_game_user(possible_moves):  # Funkcja, która jest uruchamiana w przypadku gdy gracz rozpoczyna grę
    while True:
        print("Wybierz wolny numer z planszy: ")
        i = int(input())  # Wybranie numeru indeksu
        while True:
            if i in possible_moves:
                if board[i] == ' ':  # Jeśli indeks jest pusty
                    board[i] = 'X'  # Przypisujemy mu wartość 'X'
                    possible_moves.remove(i)  # I usuwamy z możliwości ruchów
                    for x in defeat:  # Sprawdzamy czy znak postawiony w indeksie wybranym przez gracza kończy grę
                        if (board[x[0]] == board[i]) and board[x[1]] == 'X' and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                        if board[x[0]] == 'X' and (board[x[1]] == board[i]) and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == board[i]):
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return

                    c = r(0, 8)  # Przypisywanie symbolu 'X' przez bota
                    if board[c] == ' ':
                        board[c] = 'X'
                    else:
                        d = r(0, 8)
                        while board[d] != ' ':
                            d = r(0, 8)
                        board[d] = 'X'
                    for x in defeat:  # Sprawdzenie czy ruch bota kończy grę
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == 'X'):
                            print("Koniec gry, wygrał gracz")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                    print("Aktualny stan gry")
                    print(board[0] + " | ", board[1] + " | ", board[2])
                    print(board[3] + " | ", board[4] + " | ", board[5])
                    print(board[6] + " | ", board[7] + " | ", board[8])
                    break

                else:
                    print("Podano zły numer, proszę zacząć od nowa")
                    return False
            elif i not in possible_moves:
                print("Podano zły numer, proszę zacząć od nowa")
                return False


def hard_game_user(possible_moves):  # Funkcja, która jest uruchamiana w przypadku gdy gracz rozpoczyna grę na średnim poziomie, na takiej zasadzie jak powyższa funkcja
    while True:
        print("Wybierz wolny numer z planszy: ")
        i = int(input())
        while True:
            if i in possible_moves:
                if board[i] == ' ':
                    board[i] = 'X'
                    possible_moves.remove(i)
                    for x in defeat:
                        if (board[x[0]] == board[i]) and board[x[1]] == 'X' and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                        if board[x[0]] == 'X' and (board[x[1]] == board[i]) and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == board[i]):
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                    if i == 4:
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 0 and board[8] == ' ':
                        c = 8
                        board[c] = 'X'
                    if i == 1 and board[7] == ' ':
                        c = 7
                        board[c] = 'X'
                    if i == 2 and board[6] == ' ':
                        c = 6
                        board[c] = 'X'
                    if i == 3 and board[5] == ' ':
                        c = 5
                        board[c] = 'X'
                    if i == 5 and board[3] == ' ':
                        c = 3
                        board[c] = 'X'
                    if i == 6 and board[2] == ' ':
                        c = 2
                        board[c] = 'X'
                    if i == 7 and board[1] == ' ':
                        c = 1
                        board[c] = 'X'
                    if i == 8 and board[0] == ' ':
                        c = 0
                        board[c] = 'X'
                    for x in defeat:
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == 'X'):
                            print("Koniec gry, wygrał gracz")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                    print("Aktualny stan gry")
                    print(board[0] + " | ", board[1] + " | ", board[2])
                    print(board[3] + " | ", board[4] + " | ", board[5])
                    print(board[6] + " | ", board[7] + " | ", board[8])
                    break

                else:
                    print("Podano zły numer, proszę zacząć od nowa")
                    return False
            elif i not in possible_moves:
                print("Podano zły numer, proszę zacząć od nowa")
                return False


def easy_game_bot(possible_moves):  # Funkcja uruchamiana gdy bot rozpoczyna grę na niskim poziomie, działa na takiej zasadzie jak powyższe funkcje
    board[4] = 'X'
    possible_moves.remove(4)
    print(board[0] + " | ", board[1] + " | ", board[2])
    print(board[3] + " | ", board[4] + " | ", board[5])
    print(board[6] + " | ", board[7] + " | ", board[8])
    while True:
        print("Wybierz wolny numer z planszy: ")
        i = int(input())
        while True:
            if i in possible_moves:
                if board[i] == ' ':
                    board[i] = 'X'
                    possible_moves.remove(i)
                    for x in defeat:
                        if (board[x[0]] == board[i]) and board[x[1]] == 'X' and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                        if board[x[0]] == 'X' and (board[x[1]] == board[i]) and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == board[i]):
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return

                    c = r(0, 8)
                    if board[c] == ' ':
                        board[c] = 'X'
                    else:
                        d = r(0, 8)
                        while board[d] != ' ':
                            d = r(0, 8)
                        board[d] = 'X'
                    for x in defeat:
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == 'X'):
                            print("Koniec gry, wygrał gracz")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            return
                    print("Aktualny stan gry")
                    print(board[0] + " | ", board[1] + " | ", board[2])
                    print(board[3] + " | ", board[4] + " | ", board[5])
                    print(board[6] + " | ", board[7] + " | ", board[8])
                    break

                else:
                    print("Podano zły numer, proszę zacząć od nowa")
                    return False
            elif i not in possible_moves:
                print("Podano zły numer, proszę zacząć od nowa")
                return False


def hard_game_bot(possible_moves):  # Funkcja uruchamiana gdy bot rozpoczyna grę na średnim poziomie, działa na takiej zasadzie jak powyższe funkcje
    b = r(0, 8)
    possible_moves.remove(b)
    board[b] = 'X'
    print(board[0] + " | ", board[1] + " | ", board[2])
    print(board[3] + " | ", board[4] + " | ", board[5])
    print(board[6] + " | ", board[7] + " | ", board[8])
    while True:
        print("Wybierz wolny numer z planszy: ")
        i = int(input())
        while True:
            if i in possible_moves:
                if board[i] == ' ':
                    board[i] = 'X'
                    possible_moves.remove(i)
                    for x in defeat:
                        if (board[x[0]] == board[i]) and board[x[1]] == 'X' and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            break
                        if board[x[0]] == 'X' and (board[x[1]] == board[i]) and board[x[2]] == 'X':
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            break
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == board[i]):
                            print("Koniec gry, wygrał komputer")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            break
                    if i == 4:
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 0 and board[8] == ' ':
                        c = 8
                        board[c] = 'X'
                    elif i == 0 and board[8] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 1 and board[7] == ' ':
                        c = 7
                        board[c] = 'X'
                    elif i == 1 and board[7] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 2 and board[6] == ' ':
                        c = 6
                        board[c] = 'X'
                    elif i == 2 and board[6] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 3 and board[5] == ' ':
                        c = 5
                        board[c] = 'X'
                    elif i == 3 and board[5] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 5 and board[3] == ' ':
                        c = 3
                        board[c] = 'X'
                    elif i == 5 and board[3] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 6 and board[2] == ' ':
                        c = 2
                        board[c] = 'X'
                    elif i == 6 and board[2] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 7 and board[1] == ' ':
                        c = 1
                        board[c] = 'X'
                    elif i == 7 and board[1] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    if i == 8 and board[0] == ' ':
                        c = 0
                        board[c] = 'X'
                    elif i == 8 and board[0] == 'X':
                        c = r(0, 8)
                        if board[c] == ' ':
                            board[c] = 'X'
                        else:
                            d = r(0, 8)
                            while board[d] != ' ':
                                d = r(0, 8)
                            board[d] = 'X'
                    for x in defeat:
                        if board[x[0]] == 'X' and board[x[1]] == 'X' and (board[x[2]] == 'X'):
                            print("Koniec gry, wygrał gracz")
                            print("Finałowy stan gry")
                            print(board[0] + " | ", board[1] + " | ", board[2])
                            print(board[3] + " | ", board[4] + " | ", board[5])
                            print(board[6] + " | ", board[7] + " | ", board[8])
                            exit()

                    print("Aktualny stan gry")
                    print(board[0] + " | ", board[1] + " | ", board[2])
                    print(board[3] + " | ", board[4] + " | ", board[5])
                    print(board[6] + " | ", board[7] + " | ", board[8])
                    break

                else:
                    print("Podano zły numer, proszę zacząć od nowa")
                    return False
            elif i not in possible_moves:
                print("Podano zły numer, proszę zacząć od nowa")
                return False


print("Wybierz tryb gry:")
print("1 - Zaczyna użytkownik, niski poziom")
print("2 - Zaczyna użytkownik, wysoki poziom")
print("3 - Zaczyna komputer, niski poziom")
print("4 - Zaczyna komputer, wysoki poziom")
w = int(input())  # Wybór strony, która rozpoczyna grę
if w == 1:
    print()
    easy_game_user(possible_moves)
elif w == 2:
    print()
    hard_game_user(possible_moves)
elif w == 3:
    print()
    easy_game_bot(possible_moves)
elif w == 4:
    print()
    hard_game_bot(possible_moves)
else:
    print("Podany numer jest niepoprawny, uruchom program ponownie")
