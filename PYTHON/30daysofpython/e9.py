def add_two_num(a, b):
    suma = a + b
    return suma

print(add_two_num(8,7))

def area_of_circle(r):
    pi = 3.14
    area = pi * (r)**2
    return area

print(area_of_circle(2))

# SUMA DE NUMEROS PREDEFINIDOS
lista_nums = []
def add_all_nums(*numeros):
    total_suma = 0
    for i in numeros:
        if not isinstance(i, int): #verifica la clase de los argumentos 
            return "Error, todos los argumentos deben ser números enteros"
        total_suma += i
    return total_suma

print(add_all_nums(3,4,5))

def temperature_conver(v_celsius, v_farenheit):
    c_to_f = (v_celsius*(9/5)) + 32
    f_to_v = (v_farenheit-32)*(5/9)
    print(f'''Tus °{v_celsius}C en °F es: {c_to_f:.2f}
Tus °F {v_farenheit} en °C es: {f_to_v:.2f}''')

temperature_conver(20,30)

def check_season(mes):
    autumn = ["Marzo", "Abril", "Mayo"]
    winter = ["Junio", "Julio", "Agosto"]
    spring = ["Septiembr", "Octubre", "Noviembre"]
    summer = ["Diciembre", "Enero", "Febrero",]
    if mes in autumn:
        print("Estamos en Otoño")
    elif mes in winter:
        print("Estamos en Invierno")
    elif mes in spring:
        print("Estamos en Primavera")
    elif mes in summer:
        print("Estamos en Verano")
    else:
        print("Has ingresado un valor invalido")

mes = input("Enter the current month: ").title()
check_season(mes)

def calculate_slope(x1, y1, x2, y2):
    if (y2-y1) == 0:
        return "El denominador no puede ser 0"
    
    slope = (x2-x1)/(y2-y1)
    return slope

print(f'{calculate_slope(3,2,4,5):.2f}')



def solve_quadratic_eqn(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is negative (no real solutions)
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        # One real solution
        x = -b / (2*a)
        return x
    else:
        # Two real solutions
        sqrt_discriminant = discriminant**0.5  # Calculate square root without math module
        x1 = (-b + sqrt_discriminant) / (2*a)
        x2 = (-b - sqrt_discriminant) / (2*a)
        return x1, x2

# Example usage:
a = 1
b = -3
c = 2
solutions = solve_quadratic_eqn(a, b, c)
print(solutions)



