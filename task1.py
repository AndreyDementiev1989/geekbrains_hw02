# -*- coding: utf-8 -*-
'''Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
 Числа и знак операции вводятся пользователем.
 После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
'''
while True:
    actadd = str(input('Введите знак операции(+-/*) либо 0 для выхода: '))
    if actadd == '0':
        break
    else:
        a = float(input('Введите первое число: '))
        b = float(input('Введите второе число: '))
        if actadd == '+':
            print('{} + {} = {}'.format(a,b,a+b))
        elif actadd == '*':
            print('{} * {} = {}'.format(a, b, a * b))
        elif actadd == '/':
            if b != 0:
                print('{} / {} = {}'.format(a, b, a / b))
            else: print('Деление на ноль запрещено')
        else:
            print('{} - {} = {}'.format(a, b, a - b))







