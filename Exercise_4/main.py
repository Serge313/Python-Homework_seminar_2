"""Задача 4: Требуется вывести все целые степени двойки
(т.е. числа вида 2k), не превосходящие числа N."""


import sys


def powers_of_two_to_n(empty_list, number):
    """The method finds powers of two to number N"""
    power = 0
    while number > (pow(2, power)):
        empty_list.append(power)
        power += 1
    return empty_list


def testing_powers_of_two_to_n(test_number=10, test_list=[]):
    """The method tests testing_powers_of_two_to_n method"""
    print("Testing of the \"testing_powers_of_two_to_n\" method has been launched...")
    expected = [0, 1, 2, 3]
    actual = powers_of_two_to_n(test_list, test_number)
    is_equal = expected == actual
    if is_equal:
        print("Test completed successfully!")
    else:
        print("Error! Need to fix the method!")


testing_powers_of_two_to_n()
print()


try:
    n = int(input("Enter number \"N\": "))
except ValueError as ex:
    print(f"Error: {ex}")
    sys.exit()


empty_powers_of_two = []
powers_of_two = powers_of_two_to_n(empty_powers_of_two, n)
print(f"Powers of number 2 to number {n}: {powers_of_two}")
