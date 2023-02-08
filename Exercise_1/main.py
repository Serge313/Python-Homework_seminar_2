"""Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза:
один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!
Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза"""


import sys


def fill_list_of_melons(list, n):
    """The method fills empty list"""
    count = 1
    while count <= n:
        try:
            watermelon = int(input(f"Enter weight of melon number {count}: "))
        except ValueError as ex:
            print(f"Error: {ex}")
            sys.exit()
        list.append(watermelon)
        count += 1
    return list


def find_max_min_mellon(list, maximum=0, minimum=sys.maxsize):
    """The method finds max and min value of the list"""
    for i in list:
        if i > maximum:
            maximum = i
    for i in list:
        if i < minimum:
            minimum = i
    return maximum, minimum


def testing_find_max_min_mellon(test_list=[5, 1, 6, 5, 9]):
    """The method tests find_max_min_mellon method"""
    print("Testing of the \"find_max_min_mellon\" method has been launched...")
    expected = (9, 1)
    actual = find_max_min_mellon(test_list)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_find_max_min_mellon()
print()


try:
    number_of_watermelons = int(input("Enter number of watermelons: "))
except ValueError as e:
    print(f"Error: {e}")
    sys.exit()


list_of_melons = []
filled_list_of_melons = fill_list_of_melons(list_of_melons, number_of_watermelons)
RESULT = find_max_min_mellon(filled_list_of_melons)
print()
print(f"Tne number of watermelons -> {number_of_watermelons} \n"
      f"Weight of each watermelon -> {filled_list_of_melons} \n"
      f"Max and min weight of watermelons -> {RESULT}")
