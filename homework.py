# 1.Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# from math import pi

# d =  int(input("Введите число  точности:\n"))
# print(round(pi, d))

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N =  int(input("Введите число N:"))
# def number(n):
#         result=list()
#         d=2
#         while d<=n:
#             if n%d==0:
#                 result.append(d)
#                 n=n/d
#             else:
#                 d+=1
#         return result

# print (number(N))
  
# 3.Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

number= [1,5,2,6,8,6,7,4,2]
list=[]
for i in number:
    if number.count(i)==1:
        list.append(i)
print(list)



# 4.Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.