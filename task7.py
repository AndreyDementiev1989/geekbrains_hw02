''' Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n – любое натуральное число'''

n = int(input('Введите n для проверки:'))
summ_one = 0
for i in range(1, n + 1):
    summ_one += i
print(summ_one)

summ_two = n * (n + 1) / 2
print(int(summ_two))


if int(summ_one) == int(summ_two):
    print('Левая последовательность равно правой')