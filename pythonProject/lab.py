import random


class InvalidMoveError(Exception):
    pass


def get_random_stones():
    return random.randint(4, 30)


def get_user_move(remaining_stones):
    while True:
        try:
            user_input = input(
                f"Выберите количество камней (1, 2, или 3), чтобы взять из {remaining_stones} остатков: ")
            move = int(user_input)
            if move < 1 or move > 3:
                raise InvalidMoveError(f"Некорректный ввод: {move}. Вы можете взять только 1, 2 или 3 камня.")
            if move > remaining_stones:
                raise InvalidMoveError(
                    f"Некорректный ввод: {move}. Нельзя взять больше оставшихся камней ({remaining_stones}).")
            return move
        except ValueError:
            print("Пожалуйста, введите целое число.")
        except InvalidMoveError as e:
            print(e)


def computer_move(remaining_stones):
    move = min(3, remaining_stones)
    print(f"Компьютер взял {move} камня(ей).")
    return move


remaining_stones = get_random_stones()
print(f"Начинаем игру! У нас есть {remaining_stones} камней.")

while remaining_stones > 0:
    user_move = get_user_move(remaining_stones)
    remaining_stones -= user_move
    print(f"После вашего хода осталось {remaining_stones} камней.")

    if remaining_stones == 0:
        print("Поздравляем! Вы выиграли!")
        break

    computer_move_amount = computer_move(remaining_stones)
    remaining_stones -= computer_move_amount
    print(f"После хода компьютера осталось {remaining_stones} камней.")

    if remaining_stones == 0:
        print("Компьютер выиграл!")
