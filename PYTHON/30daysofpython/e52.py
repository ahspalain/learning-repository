ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)
mediana = (ages[5]+ages[6])/2
print(mediana)
average_age = sum(ages)/len(ages)
print(average_age)
range_ages = max(ages) - min(ages)
print(range_ages)
print(abs(min(ages)) == abs(max(ages)))



