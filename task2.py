#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


def task():
    try:
        import random

        strk = int(input('Введите количество строк >>> '))
        stlb = int(input('Введите количество столбцов >>> '))
        start = int(input('Начало диапазона целых чисел >>> '))
        finish = int(input('Конец диапазона целых чисел >>> '))
        list_1 = [[randint(start, finish) for i in range(strk)] for i in range(stlb)]
        for i in list_1:
            print()
            for a in i:
                print(a, end=" ")
    except ValueError:
        print("Ошибка, попробуйте еще раз")
    else:
        print("\nВыполненно без ошибок")
    finally:
        print("Программа завершила работу")


if __name__ == '__main__':
    task()
