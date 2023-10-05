age = int(input("Enter your age: "))
age_needed = 18

print(f'You can learn to drive') if age >= age_needed else print(f'You need {age_needed-age} years to learn to drive') 

your_age = int(input("Enter your age: "))
my_age = 24
dif = your_age - my_age
dif2 = my_age - your_age

if your_age > my_age:
    print("You are %d year(s) older than me" %(dif))
elif your_age < my_age:
    print("You are %d year(s) younger than me" %(dif2))
else:
    print("We have the same age") 

calificacion = int(input("Enter your score: "))

if 90 <= calificacion <= 100:
    print("ur grade is A")

elif 70 <= calificacion <= 89:
    print("ur grade is B")

elif 60 <= calificacion <= 69:
    print("ur grade is C")

elif 50 <= calificacion <= 59:
    print("ur grade is D")

else:
    print("ur grade is F")

season = input("Enter the actual month: ").lower()
autumn = ["september", "october", "november"]
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]

if season in autumn:
    print("Es otoño")

elif season in winter:
    print("Es invierno")

elif season in spring:
    print("Es primavera")

elif season in summer:
    print("Es verano")

else:
    print("Ingresaste un mes incorrecto")

fruits = ['banana', 'orange', 'mango', 'lemon']

new_fruit = (input("Enter a fruit to add to the list: ")).lower()

if new_fruit not in fruits:
    fruits.append(new_fruit)
    print(f'Esta es la nueva lista {fruits}')

else:
    print("That fruit already exist in the list")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

