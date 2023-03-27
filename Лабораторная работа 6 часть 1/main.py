from __future__ import annotations
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from plot import plot_area
from parse_table import get_table


def main():
    print('Введите данные или оставьте поле пустым')
    
    variance = validate_data(input('Введите значение дисперсии: '))
    std = validate_data(input('Введите значение среднеквадратического отклонения: '))
    selection = validate_data(input('Введите значение выборки: '))   
    sample_mean = validate_data(input('Введите значение выборочной средней: '))
    significance_level = validate_data(input('Введите значение уровня значимости: '))
    H0 = validate_data(input('Введите значение нулевой гипотезы: '))
    H1 = validate_data(input('Введите значение конкурирующей гипотезы: '))

    critical_area, area = get_critical_area(H0, H1, significance_level)
    print(critical_area)
    
    plot_area(critical_area, area)
    
    U = get_u(critical_area)
        
    Unabl = get_test_statistic(std, variance, sample_mean, selection, H0)
    print(analyse(U, Unabl, area))
    
    
def get_test_statistic(std, variance, sample_mean, selection, H0) -> float:
    if variance != None:
        test_statistic = ((sample_mean - H0) * sqrt(selection)) / sqrt(variance)
    else:
        test_statistic = ((sample_mean - H0) * sqrt(selection)) / std
    
    return test_statistic
        
        
def validate_data(number) -> float:
    try:
        number = float(number)
    except ValueError:
        number = None
    return number


def get_critical_area(H0, H1, a) -> tuple:
    
    if H1 < H0:
        area = 'left'
    elif H1 > H0:
        area = 'right'      
    else:
        area = 'two-sided'
    
    if area == 'left' or area == 'right':
        U = (1 - 2 * a) / 2
    else:
        U = (1 - a) / 2
    return U, area
   
   
def get_u(f):
    table = get_table()
    for i in table:
        if float(i) > f:
            return float(table[i])
    

def analyse(U, Unabl, area):
    print(U, Unabl)
    if area == 'left':
        if Unabl > -U:
            return 'Гипотеза принимается'
        else:
            return 'Гипотеза отвергается'
   
    elif area == 'right':
        if Unabl < U:
            return 'Гипотеза принимается'
        else:
            return 'Гипотеза отвергается'
    
    else:
        if -U < Unabl < U:
            return 'Гипотеза принимается'
        else:
            return 'Гипотеза отвергается'


if __name__ == '__main__':
    main()