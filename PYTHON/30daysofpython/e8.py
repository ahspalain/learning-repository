for i in range(11):
    print(i)

number = 10
for j in range(11):
    print(number)
    number -= 1

for k in range(7):
    print("#"*(k+1))

for x in range(8):
    for y in range(8):
            print("#", end=" ")
    print()

for l in range(11):
     for m in range(11):
          print(f'{l} * {m} = {l * m}')
     print()

it_lang = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in it_lang:
     print(item)

for pares in range(0,101,2):
     print(pares)

for impares in range(1,101,2):
     print(impares)

total_sum_pares = 0
total_sum_impares = 0
for a in range(0, 101,2):
     total_sum_pares += a

for b in range(1, 101,2):
     total_sum_impares += b
    
print(f'sum of all evens is {total_sum_pares}, sum of total odds is {total_sum_impares}')

fruit = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruit)-1,-1,-1):
     print(fruit[i])





