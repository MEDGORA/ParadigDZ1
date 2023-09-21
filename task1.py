"""
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
"""


numbers = [3,6,4,7,12,1,5,0,4,4]  
numbers2 = [3,6,4,7,12,1,5,0,4,4,324,3543,4534]  
print('Задание 1')
print('начальный массив: ', numbers)


for i in range(len(numbers)) :
  indexOfMax = 0
  max = numbers[i]
  for j in range(i, len(numbers)) :
    if numbers[j] >= max and numbers[j] >= numbers[i]: 
      max = numbers[j] 
      indexOfMax = j 
  numbers[indexOfMax] = numbers[i] 
  numbers[i] = max 

print('импеативный: ', numbers)
print()



"""Написать точно такую же процедуру, но в декларативном стиле"""

print('Задание 2')
print('начальный массив: ', numbers2)


numbers2.sort(reverse=True) 

print('декларативный: ', numbers2)
print()
