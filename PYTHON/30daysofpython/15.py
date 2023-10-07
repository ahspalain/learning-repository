
with open("sexo.txt", 'a') as f:
    f.write("This text has to be appended at the end")
f.close()

with open('sexo2.txt','w') as f:
    f.write('This text will be written in a newly created file')
f.close()

print(open("sexo.txt", 'r'))
print(open("sexo2.txt", 'r'))

import os
os.remove('sexo2.txt')

if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

