from ordenes import Orden_divc
from computadora import Computadora_divc
from dispositivo import Dispositivo_entrada
from teclados import Teclado_divc
from ratones import Raton_divc
from monitor import Monitor_divc

teclado1 = Teclado_divc("USB", "Lenovo")
raton1 = Raton_divc("Bluetooth", "Razer")
monitor1 = Monitor_divc("Samsung", "42 pulgadas")

computadora1 = Computadora_divc("Oficina", monitor1, teclado1, raton1)

teclado2 = Teclado_divc("USB", "Lenovo")
raton2 = Raton_divc("Bluetooth", "Razer")
monitor2 = Monitor_divc("Samsung", "42 pulgadas")

computadora2 = Computadora_divc("Gamer", monitor1, teclado1, raton1)

computadoras1 = [computadora1, computadora2]
orden1 = Orden_divc(computadoras1)
print(orden1)
