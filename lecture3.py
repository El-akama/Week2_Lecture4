# list_ = list()
# list_ = []
# list_ = list('hello')
# print(list_)

# a = "hello"
# b = a.replace('l', 'k')
# print(b)

# a = [1, 2, 3, 4, 5, 6, 'a']
# b = ['a', 'b']
# c = a * 3
# a[-1] = a[-1] * 3                   # запомнить как дублировать внутри списка
# a.pop()
# print(a)

# print(len(a))

# a[1] = 5                      # замена элемента в списке без метода

# a.insert(0, 0)                  # замена с методом  
# print(a)

# a = a[2::2]
# print(a)

# del a[3]                # удаление элемента с помощью del

# del a                   # удаляет весь список

# a.extend(b)             # расширение списка А с помощью Б
# print(a)


# КОРТЕЖ - Tuple

# a = ()
# a = tuple([1, 2, 3])
# print(a)

# c = (1,)                    # кортеж из одного элемента, то надо в конце ставть запятую

# a = ('a', 1, 2, False, None, [1, 2], {'key': 'value'}, (4,))
# # print(a.count('a'))

# print(a.index([1, 2]))
# a[5][0] = 5                 # если в кортеже есть изменяемый типы данных, то его можно изменить
# print(a)

# a = 2
# b = 3
# c = a
# a = b
# b = c

# a, b = b, a               # множественное присваивание
# print(a, b)

# a = 1, 'a'
# print(a)

# a = (1, 2, 3)
# b, c, d = a               # анпакинг когда элементов одинаково
# print(a)
# print(b)
# print(c)
# print(d)

# a = (1, 2, 3, 4)
# b, c, *d = a              #  анпакинг когда некоторых переменных больше юзаем звездочку
# print(a)
# print(b)
# print(c)
# print(d)