from ratones import Raton_divc
from teclados import Teclado_divc
from monitor import Monitor_divc

class Computadora_divc:

    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton) -> None:
        Computadora_divc.contador_computadoras += 1
        self._id_computadora = Computadora_divc.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self) -> str:
        return f'''
            {self._nombre}: {self._id_computadora}
                Monitor: {self._monitor}
                Teclado: {self._teclado}
                Ratón: {self._raton}
        '''

if __name__ == "__main__":
    teclado1 = Teclado_divc("USB", "Lenovo")
    raton1 = Raton_divc("Bluetooth", "Razer")
    monitor1 = Monitor_divc("Samsung", "42 pulgadas")

    computadora1 = Computadora_divc("PC1", monitor1, teclado1, raton1)
    print(computadora1)