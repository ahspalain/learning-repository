import random
import string

# def generate_random_user_id():
#     # Define the characters to choose from
#     characters = string.ascii_letters + string.digits  # Letters (both uppercase and lowercase) and digits

#     # Use random.choices to generate a six-character random user ID
#     random_user_id = ''.join(random.choices(characters, k=6))   

#     return random_user_id

# # Example usage:
# user_id = generate_random_user_id()
# print(user_id)

# def user_id_ge_by_user():
#     letter_of_id = string.ascii_letters + string.digits
#     how_much_ids = int(input("Enter the num of IDs u wanto to generate: "))
#     how_long = int(input("Enter the num of character to your ID: "))
#     list_ids = set()
#     generated_ids = 0
#     for _ in range(how_much_ids):
#         random_new_id = ''.join(random.choices(letter_of_id, k=how_long))
#         if random_new_id not in list_ids:
#             list_ids.add(random_new_id)
#             generated_ids += 1
#     print(f'''These are your new ID's:
# ''')
#     for user_id in list_ids:
#         print(user_id)


# user_id_ge_by_user()


# def rgb_color_gen():
#     # Generar valores aleatorios para los componentes R, G y B
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)

#     return f'rgb({r}, {g}, {b})'

# print(rgb_color_gen())


# def list_of_hexa_colors():
#     format_hexa_color = string.hexdigits
#     new_hex_color = "#" + ''.join(random.choices(format_hexa_color,k=6))
#     return new_hex_color

# print(list_of_hexa_colors())

def gemerate_colors(type, cantidad):
    format_hexa_color = string.hexdigits
    list_rgb = []
    list_hexa = []

    if type == "rgb":
        for _ in range(cantidad):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            rgb_color_1 = f'rgb({r}, {g}, {b})'
            list_rgb.append(rgb_color_1)
        return list_rgb
    
    elif type == "hexa":
        for _ in range(cantidad):
            new_hex_color = "#" + ''.join(random.choices(format_hexa_color,k=6))
            list_hexa.append(new_hex_color)
        return list_hexa
    
    else:
        return f'Has introducido valores invalidos'
    

print(gemerate_colors("hexa", 3))


import random

def shuffle_list(input_list):
    shuffled_list = input_list.copy()  # Copia la lista original para no alterarla
    random.shuffle(shuffled_list)      # Mezcla la lista de forma aleatoria
    return shuffled_list

# Ejemplo de uso
original_list = [1, 2, 3, 4, 5]
shuffled_result = shuffle_list(original_list)
print("Lista original:", original_list)
print("Lista mezclada:", shuffled_result)


import random

def unique_random_numbers():
    numbers = list(range(10))  # Create a list of numbers from 0 to 9
    random.shuffle(numbers)    # Shuffle the list randomly
    unique_numbers = numbers[:7]  # Select the first 7 numbers after shuffling
    return unique_numbers

# Example usage
random_numbers = unique_random_numbers()
print(random_numbers)

def unique_random_nums_gen():
    nums1 = string.digits
    random_numbers_1 = random.sample(nums1,7)
    return random_numbers_1

print(unique_random_nums_gen())


















