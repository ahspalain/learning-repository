import re

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."

# Dividir el párrafo en palabras
words = re.findall(r'\w+', paragraph.lower())  # Convertir a minúsculas para no ser sensible a mayúsculas/minúsculas

# Crear un diccionario para llevar un registro de las frecuencias de las palabras
word_freq = {}

# Contar la frecuencia de cada palabra
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Encontrar la palabra más frecuente
most_common_word = max(word_freq, key=word_freq.get)
frequency = word_freq[most_common_word]

print(f'La palabra más frecuente es "{most_common_word}" con {frequency} apariciones.')
print(word_freq)



points = ['-12', '-4', '-3', '-1', '0', '4', '8']

# Utilizar expresiones regulares para extraer números de las cadenas
pattern = r'-?\d+'  # Coincide con números enteros, incluyendo signos negativos
numbers = [int(match) for match in re.findall(pattern, ' '.join(points))]

# Ordenar la lista de números
sorted_points = sorted(numbers)

# Calcular la distancia entre el valor máximo y el valor mínimo
distance = sorted_points[-1] - sorted_points[0]

print(sorted_points)  # [-12, -4, -3, -1, -1, 0, 4, 8]
print(distance)       # 20



def clean_text(text):
    # Eliminar caracteres especiales y signos de puntuación
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convertir a minúsculas y dividir en palabras
    words = cleaned_text.lower().split()
    
    # Devolver el texto limpio y las palabras divididas
    return cleaned_text, words

def most_frequent_words(words, n=3):
    word_counts = {}
    
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Encontrar las n palabras más frecuentes
    most_common = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]
    
    return most_common

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Limpiar el texto y obtener las palabras
cleaned_text, words = clean_text(sentence)

print(cleaned_text)  # Texto limpio
print(most_frequent_words(words))  # Las tres palabras más frecuentes
