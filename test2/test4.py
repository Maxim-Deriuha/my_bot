m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
     'ножницы-ножницы': 'ничья','ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
     "бумага-бумага": 'ничья','бумага-камень': 'Тимур','бумага-ножницы': 'Руслан'}
a = input()
b = input()
ab = a + '-' + b
print(m[ab])