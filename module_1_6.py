
my_dict={'Lena': 1977, 'Ludmila': 1948, 'Max': 1998}
print(my_dict)
print(my_dict.get('Lena'))
print(my_dict.get('Ernest'))
my_dict.update({'Katya': 2000, 'SaSha': 2024})
removed_year = my_dict.pop('SaSha')
print(removed_year)
print(my_dict)



my_set = {1, 2, 3, 4, 3, 3, 2, 5, True, True, False, True, 'стенка', 'стенка', 'потолок', 'аффирмация'}
print(my_set)
my_set.add('искусство',)
my_set.add('любить')
my_set.discard(2)
print(my_set)