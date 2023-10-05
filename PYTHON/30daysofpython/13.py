countries = ["Finland", "Perú"]

for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
        
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6, 7]
# lst = [0, *lst_one, *lst_two]
# print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
# country_lst_one = ['Finland', 'Sweden', 'Norway']
# country_lst_two = ['Denmark', 'Iceland']
# nordic_countries = [*country_lst_one, *country_lst_two]
# print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)


p_paises = ['Finlandia', 'Suecia', 'Noruega','Dinamarca','Islandia', 'Estonia','Rusia']
*list5f, es, ru = p_paises

nordic_countries = [list5f]
es_pas = [es]
rusia = [ru]

print(nordic_countries)
print(es_pas)
print(rusia)
