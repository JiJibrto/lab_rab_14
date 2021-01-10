#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
# соединение, строк. В остальных случаях введенные числа суммируются.


def number():

    a = input("Enter a> ")
    b = input("Enter b> ")
    try:
        if int(a) and int(b):
            c = int(a) + int(b)
            print(c)
    except ValueError:
        print(a + b)


if __name__ == '__main__':
    number()
