empty_list = []
list1 = ["pene", "teta", "concha", "culo", "chocha"]
print(len(empty_list))
print(len(list1))
print(list1[2:3])
mixed_data_types = ["Adrian", 24, 1.80,["Marital Status: Single"], "Enrique Pallardelli 449 Urb El Retablo Comas"]
print(mixed_data_types)
companys = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(companys)
print(len(companys))
print(companys[0::3])
companys[0] = "Rappi"
print(companys)
companys.append("Fallabella")
print(companys)
companys.insert(4,"Yape")
print(companys)
companys[4] = "Rappi".upper()
print(companys)
michi = "#"
companys.extend(michi)
print(companys)
print("RAPPI" in companys)
companys.sort()
print(companys)
companys.sort(reverse=True)
print(companys)
companys.pop(0)
companys.pop(1)
companys.pop(2)
print(companys)