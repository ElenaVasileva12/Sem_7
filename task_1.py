# Напишите функцию группового переименования файлов. Она должна:
# 1) принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# 2) принимать параметр количество цифр в порядковом номере.
# 3) принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# 4) принимать параметр расширение конечного файла.
# 5) принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from string import ascii_lowercase
import random as rnd

letter=ascii_lowercase

def generate_name(): #случайное имя
    size=rnd.randint(4,7)
    name=rnd.sample(letter,size)
    name.append(rnd.choice(letter))
    rnd.shuffle(name)
    name=''.join(name).title()
    return name


def renaming(new_name_file,count_,expansion_old,expansion_new,range_):
  data=list(map(str,[rnd.randint(1,9) for i in range(count_)])) # количество цифр в порядковом номере.
  k=int(''.join(data))
  for i in os.listdir():
    name = os.path.splitext(i)[1] #ищем расширение
    old_name_file = name[range_[0]:range_[1]] if range_ else ""
    if name == expansion_old:
      os.rename(i,f'{old_name_file}{new_name_file}_{k}{expansion_new}') #имя старое,имя новое,_номер.расширение_новое
      k+=1

new_name= generate_name()
renaming(new_name,3,'.txt','.dat', [1,3]) #,'.dat','.txt',