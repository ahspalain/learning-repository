from dispositivo import Dispositivo_entrada

class Teclado_divc(Dispositivo_entrada):
    contador_teclado = 0

    def __init__(self, tipoentrada, marca) -> None:
        Teclado_divc.contador_teclado +=1
        super().__init__(tipoentrada, marca)
        self._id_teclado = Teclado_divc.contador_teclado

    def __str__(self) -> str:
        return f'id: {self._id_teclado}, {super().__str__()}'

if __name__ == "__main__":   
    teclado1 = Teclado_divc("bluetooth", "lenovo")
    print(teclado1)

    teclado2 = Teclado_divc("USB", "razer")
    print(teclado2)