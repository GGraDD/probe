#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family = ['жена', 'дочка', 'сын']
print(my_family)
my_family_height = [['Лена', 170 ],['Инара', 112 ],['Яромир', 70 ]]
print(my_family_height)
# список списков приблизителного роста членов вашей семьи
# ['имя', рост],
rost_wife=my_family_height[0][1]
text_1='Рост жены -'
text_2="см"
print((text_1),(rost_wife),(text_2))
rost_family=my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]
rost_family_text='Рост всей семьи -'
print((rost_family_text),(rost_family),(text_2))
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

