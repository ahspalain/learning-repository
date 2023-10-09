nums = [9, 4, 40, 35, 44, 22, 6, 25]

# Crear una lista vacía para almacenar los valores únicos ordenados
sorted_nums = []

for num in nums:
    if num not in sorted_nums:
        sorted_nums.append(num)

# Implementar el algoritmo de selección para ordenar la lista
for i in range(len(sorted_nums)):
    min_idx = i
    for j in range(i + 1, len(sorted_nums)):
        if sorted_nums[j] < sorted_nums[min_idx]:
            min_idx = j
    # Intercambiar los elementos
    sorted_nums[i], sorted_nums[min_idx] = sorted_nums[min_idx], sorted_nums[i]

print(sorted_nums)
