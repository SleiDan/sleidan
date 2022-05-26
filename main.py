from random import *
from time import *

def sequances():
    bit = 8
    N = 4096
    while bit <= 4096:
        print(f"{bit}-битная последовательность имеет {2**bit} вариантов")
        bit*=2


def bit_num(number_of_bits):
    return randint(1,1 << number_of_bits)


def brutforce(num):
    i = 0
    time_start = time()
    while True:
        if num == i:
            time_end = time()
            print(f"Потраченное время: {int(round((time_end - time_start) * 1000))} ms")
            break
        i+=1
    return i


sequances()
print('Введите число для бутфорса:')
bit = int(input())
num = bit_num(bit)
print(f'Случайное значение ключа: {num}')
brutforce(num)