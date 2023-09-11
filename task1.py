"""  Напишите функцию, которая принимает на вход строку — 
абсолютный путь до файла. Функция возвращает кортеж из трёх 
элементов: путь, имя файла, расширение файла. """
import os
from typing import Any


str_ = 'file://srv03/RFolders$/%D0%97%D0%B0%D0%BC%D0%B3%D0%BB%D0%B0%D0%B2%D0%B1%D1%83%D1%85/Downloads/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%B8%D1%87%D0%BA%D0%B0%204.%20%D0%9F%D0%BE%D0%B3%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B2%20Python.%20%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B8.pdf'

def split_path_1(txt):
    *a, b = txt.split('/')
    return '/'.join(a), *b.split('.')


def split_path_2(path: str) -> tuple[str, Any]:
    return os.path.split(path)[0], *os.path.split(path)[1].split('.')

print(split_path_1(str_))
print(split_path_2(input('Введите путь: ')))