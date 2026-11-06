from collections.abc import Callable
import re

def generator_numbers(text: str):
    formated_str1 = re.sub(r'[^\d\.]+', ' ', text) #remove all characters except digits and dots
    formated_str2 = re.sub(r'(?<!\d)\.(?!\d)', '', formated_str1) #remove dots that are not part of a number
    print(formated_str2)
    for num in formated_str2.split():
        num = float(num)
        yield num

def sum_profit(text: str, func: Callable):
    total = 0
    for num in func(text):
        total += num
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")