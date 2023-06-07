"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def count_product_avg(sales):
    items_sold_sum = 0
    for item_sold in sales:
        items_sold_sum += item_sold
    items_sold_avg = items_sold_sum / len(sales)
    return items_sold_avg

products_sum = 0
for one_product in products:
    items_sold_sum = sum(one_product['items_sold'])
    print(f'Сумманое количество продаж товара {one_product["product"]}: {items_sold_sum}')
    products_sum += items_sold_sum

products_avg_sum = 0
for one_product in products:
    items_sold_avg = round(count_product_avg(one_product['items_sold']), )
    print(f'Среднее количество продаж товара {one_product["product"]}: {items_sold_avg}')
    products_avg_sum += items_sold_avg

products_len_sum = 0
for one_product in products:
    items_sold_1 = len(one_product['items_sold'])
    products_len_sum += items_sold_1

print(f'Сумманое количество продаж всех товаров: {products_sum}')


products_avg = round(products_sum/products_len_sum, )
print(f'Среднее количество продаж всех товаров: {products_avg}')
