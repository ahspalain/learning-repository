
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mayusculas_xpalabra(palabras):
    return palabras.upper()
    
resultado = map(mayusculas_xpalabra,countries)
print(list(resultado))

def square_number(numb):
    return numb**2

resultado1 = map(square_number, numbers)
print(list(resultado1))

resultado2 = map(mayusculas_xpalabra,names)
print(list(resultado2))


def ends_with_land(country):
    return country[-4:] == "land"

countries_w_land = filter(ends_with_land, countries)
print(list(countries_w_land))

def delete_countrys_len_6(country):
    return len(country) == 6

filtered_countries = filter(delete_countrys_len_6, countries)
print(list(filtered_countries))

def delete_countrys_len_equal6(country):
    return len(country) >= 6

filtered_countries = filter(delete_countrys_len_equal6, countries)
print(list(filtered_countries))

def countries_start_w_e(country):
    return country[0] == "E"

countri_e = filter(countries_start_w_e,countries)
print(list(countri_e))

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = (
    reduce(lambda x, y: x + y,           # Reducción: suma
        filter(lambda x: x % 2 == 0,     # Filtrado: números pares
            map(lambda x: x * 2,         # Mapeo: duplicar números
                numeros
            )
        )
    )
)

print(resultado)  # Imprimir el resultado

list1 = [1, "papa", 3, "mamá"]

def get_string_list(word):
    return isinstance(word,str)

word_str = filter(get_string_list,list1)
print(list(word_str))

def summ_num_list(a,b):
    return a+b

suma_de_numeros = reduce(summ_num_list, numbers)
print(suma_de_numeros)

from functools import reduce

from functools import reduce

# Lista de países
paises = ['Estonia', 'Finlandia', 'Suecia', 'Dinamarca', 'Noruega', 'Islandia']

# Definir una función para concatenar países con comas y "y"
def concatenar_paises(resultado, pais):
    if resultado == "":
        return pais
    elif pais == paises[-1]:
        return f"{resultado}, y {pais}"
    else:
        return f"{resultado}, {pais}"

# Utilizar reduce para concatenar los países
paises_concatenados = reduce(concatenar_paises, paises)

# Crear la oración deseada
oracion = f"{paises_concatenados} son países del norte de Europa."

# Imprimir la oración
print(oracion)

def count_countries_by_starting_letter(countries):
    # Create an empty dictionary to store the counts
    letter_counts = {}

    # Iterate through the countries
    for country in countries:
        # Get the first letter of the country name
        first_letter = country[0]

        # Check if the letter is already in the dictionary
        if first_letter in letter_counts:
            # If it is, increment the count
            letter_counts[first_letter] += 1
        else:
            # If it's not, add it to the dictionary with a count of 1
            letter_counts[first_letter] = 1

    return letter_counts

# List of countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

# Call the function and print the result
country_counts = count_countries_by_starting_letter(countries)
print(country_counts)


def get_first_ten_countries(country_list):
    return country_list[:10]

# Example list of countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Canada', 'Mexico', 'United States', 'Brazil', 'Argentina', 'Chile']

# Call the function to get the first ten countries
first_ten = get_first_ten_countries(countries)

# Print the result
print(first_ten)


def get_first_ten_countries(country_list):
    return country_list[:10]

# Example list of countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Canada', 'Mexico', 'United States', 'Brazil', 'Argentina', 'Chile']

# Call the function to get the first ten countries
first_ten = get_first_ten_countries(countries)

# Print the result
print(first_ten)


def get_first_ten_countries(country_list):
    return country_list[-10:]

# Example list of countries
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Canada', 'Mexico', 'United States', 'Brazil', 'Argentina', 'Chile']

# Call the function to get the first ten countries
first_ten = get_first_ten_countries(countries)

# Print the result
print(first_ten)


