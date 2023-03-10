"""
4. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Далее необходимо собрать аналитику о товарах. Реализовать словарь,
в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.

Пример:

{
“названия”: [“компьютер”, “принтер”, “сканер”],
“цены”: [20000, 6000, 2000],
“количества”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

num = int(input('Введите количество товарных позиций: '))
product = tuple()
list_product = []
dict_product = dict()
char_product = ['название', 'цена', 'количество', 'ед']
name = []
price = []
quantity = []
unit = []
list_val = [name, price, quantity, unit]

analitic = dict()
i = 0
while i < num:
    dict_product = dict({'название': input('Введите название товара: '),
                'цена': float(input('Введите цену товара: ')),
                'количество': int(input('Введите количество товара: ')),
                'ед': input('Введите единицу измерения товара: ')})
    name.append(dict_product['название'])
    price.append(dict_product['цена'])
    quantity.append(dict_product['количество'])
    unit.append(dict_product['ед'])
    product = (i + 1, dict_product)

    list_product.append(product)
    i += 1
print('Товары:')
i = 0
for i in range(len(list_product)):
    print(list_product[i])
    i += 1
print('Аналитика:')
analitic = dict(zip(char_product, list_val))
for key, value in analitic.items():
    print("{0}: {1}".format(key, value))
