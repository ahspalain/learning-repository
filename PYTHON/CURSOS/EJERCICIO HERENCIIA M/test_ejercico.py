from cuadrado1 import Cuadrado_figu
from rectangulo import Rectangulo_fig


print("Creación Objeto de Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado_figu(5,"rojo")
print(f'El área del cuadrado es: {cuadrado1.calc_areaC()}')
print(cuadrado1)

print("Creación Objeto de Cuadrado".center(50, "-"))
rectangulo1 = Rectangulo_fig(5,4,"negro")
print(f'El área del rectangulo es: {rectangulo1.calc_areaR()}')
print(rectangulo1)