list_1 = ["Perú", "Chile", "Argentina"]
def print_list(list_1):
    for pais in list_1:
        print(pais)


print_list(list_1)

def reverse_list(list_1):
        print(list_1[::-1])
reverse_list(list_1)

def upper_list_items(list_1):
    upper_list = []  # Initialize an empty list to store the capitalized items
    
    for item in list_1:
        upper_list.append(item.upper())
    
    return upper_list

# Example usage:
print(upper_list_items(list_1))

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']

def add_items(item):
     food_staff.append(item)
     return food_staff

print(add_items("Apple"))

numbers = [2, 3, 7, 9]

def del_items(lista1, item2):
     if item2 in lista1:
          lista1.pop(lista1.index(item2))
          return lista1
     else:
          print("Este número no se encuentra en la lista")

print(del_items(list_1,"Perú"))

def suma_nums_consecutivos(n):
     total_suma = 0
     for x in range(n+1):
        total_suma += x
     return total_suma

print(suma_nums_consecutivos(100))

def sum_of_even(even):
     total_suma2 = 0
     for y in range(0,even+1,2):
          total_suma2 += y
     return total_suma2

print(sum_of_even(10))

def sum_of_odds(odds):
     total_suma3 = 0
     for z in range(1, odds+1, 2):
          total_suma3 += z
     return total_suma3

print(sum_of_odds(100))

def even_and_odds(n):
     count_of_evens = 0
     count_of_odds = 0
     for i in range(n+1):
          if i % 2 == 0:
               count_of_evens += 1
               
          else:
               count_of_odds += 1
     return f'''The number of evens are {count_of_evens}
The number of odds are {count_of_odds}'''

print(even_and_odds(100))

def factorial(number):
    count_number = 1
    for i in range(1, number+1):
         count_number *= i
    return count_number

print(factorial(5))

def is_empty(param):
    if not param:  # Check if the parameter is "falsy" (empty or evaluates to False)
        return True
    else:
        return False