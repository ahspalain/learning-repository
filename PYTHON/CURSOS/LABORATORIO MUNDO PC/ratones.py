from dispositivo import Dispositivo_entrada

class Raton_divc(Dispositivo_entrada):
    contador_raton = 0

    def __init__(self, tipoentrada, marca) -> None:
        Raton_divc.contador_raton +=1
        super().__init__(tipoentrada, marca)
        self._id_raton = Raton_divc.contador_raton

    def __str__(self) -> str:
        return f'id: {self._id_raton}, {super().__str__()}'

if __name__ == "__main__":  
    raton1 = Raton_divc("bluetooth", "lenovo")
    print(raton1)
