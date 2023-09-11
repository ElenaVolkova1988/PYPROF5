""" ✔ Создайте функцию-генератор. 
✔ Функция генерирует N простых чисел, 
начиная с числа 2. 
✔ Для проверки числа на простоту используйте 
правило: «число является простым, если делится 
нацело только на единицу и на себя». """

def prime_number(num):
    del_ = 2
    while del_ ** 2 < num and num % del_ != 0:
        del_ += 1
    return del_ ** 2 > num

def my_generator(number):
    start = 1
    while number > 1:
        start += 1
        number -= 1
        if prime_number (start):
            yield start

print(*my_generator(10))