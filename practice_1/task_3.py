# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = int(input())
height = int(input())

def bmi(weight, height):
    
    if height == 0:
        return 'Ошибка'
    else: return weight/(height**2)

print(bmi(weight, height))
#Ваш кол