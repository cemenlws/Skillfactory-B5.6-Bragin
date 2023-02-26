# Создаем список для игрового поля и заполняем его дефисами.
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Функция для вывода игрового поля.
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Функция для запуска игры
def play_game():
    current_player = "X"
    game_still_going = True

    # Главный цикл игры
    while game_still_going:
        display_board()
        position = input("Выберите позицию от 1 до 9: ")
        # Проверяем что введены только цифры
        if not position.isdigit():
            print("Некоректный ввод. Выберите позицию от 1 до 9.")
            continue

        position = int(position) - 1

        # Проверяем что введены только цифры от 1 до 9.
        if position not in range(0, 9):
            print("Некоректный ввод. Выберите позицию от 1 до 9.")
            continue

        # Если клетка пустая ставим значок текущего игрока.
        if board[position] == "-":
            board[position] = current_player
        else:
            print("Эта клетка уже занята. Выберете другю позицию.")
            continue

        # Проверяем, выиграл ли текущий игрок.
        if check_if_win():
            display_board()
            print(current_player + " Победил!")
            game_still_going = False
            # Проверяем, не наступила ли ничья.
        elif check_if_tie():
            display_board()
            print("Ничья")
            game_still_going = False

        # Переключаем текущего игрока на другого.
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# Далее проверяем все варианты победы.
def check_if_win():
    if check_rows() or check_columns() or check_diagonals():
        return True
    return False


def check_rows():
    if board[0] == board[1] == board[2] != "-":
        return True
    elif board[3] == board[4] == board[5] != "-":
        return True
    elif board[6] == board[7] == board[8] != "-":
        return True
    return False


def check_columns():
    if board[0] == board[3] == board[6] != "-":
        return True
    elif board[1] == board[4] == board[7] != "-":
        return True
    elif board[2] == board[5] == board[8] != "-":
        return True
    return False


def check_diagonals():
    if board[0] == board[4] == board[8] != "-":
        return True
    elif board[2] == board[4] == board[6] != "-":
        return True
    return False


# проверка осталось ли место на доске
def check_if_tie():
    if "-" not in board:
        return True
    return False


play_game()
