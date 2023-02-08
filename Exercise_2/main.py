"""Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть."""


import sys


class InvalidCoinSide(Exception):
    pass


def fill_list_of_coins(list, n):
    """The method fills empty list"""
    count = 1
    while count <= n:
        try:
            coin = int(input(f"Enter side of coin number {count}: "))
            if coin != 1 and coin != 0:
                raise InvalidCoinSide("Side of the coin can be entered in \"0\" / \"1\" format!")
        except InvalidCoinSide as exception:
            print(exception)
            sys.exit()
        except ValueError as ex:
            print(f"Error: {ex}")
            sys.exit()
        list.append(coin)
        count += 1
    return list


def find_number_of_flips(list):
    """The method counts number of heads and tails and minimal number of coins that must be flipped"""
    heads = 0
    for i in list:
        if i == 1:
            heads += 1
    tails = len(list) - heads
    if heads > tails:
        return tails
    else:
        return heads


def testing_find_number_of_flips(test_list=[0, 1, 1, 0, 1, 0, 0]):
    """The method tests find_number_of_flips method"""
    print("Testing of the \"find_number_of_flips\" method has been launched...")
    expected = 3
    actual = find_number_of_flips(test_list)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_find_number_of_flips()
print()


try:
    number_of_coins = int(input("Enter number of coins: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


print("Enter side of coins in \"0\" / \"1\" format, where \"1\" - heads, \"0\" - tails.")
list_of_coins = []
filled_list_of_coins = fill_list_of_coins(list_of_coins, number_of_coins)
RESULT = find_number_of_flips(filled_list_of_coins)
print()
print(f"Tne number of coins -> {number_of_coins} \n"
      f"Side of each coin -> {filled_list_of_coins} \n"
      f"Minimal number of flips -> {RESULT}")
