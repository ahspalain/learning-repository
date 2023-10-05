class Monitor_divc:

    contador_monitor = 0

    def __init__(self, marca, tamaño) -> None:
        Monitor_divc.contador_monitor += 1
        self._id_monitor = Monitor_divc.contador_monitor
        self._marca = marca
        self._tamaño = tamaño
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño
    
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    
    def __str__(self):
        return f'Id: {self._id_monitor}, Tamaño: {self._tamaño}, Marca: {self._marca}'
    

if __name__ == "__main__":
    monitor1 = Monitor_divc("Lenovo", "42 pulgadas")
    print(monitor1)
    print(monitor1.tamaño)
    monitor1.tamaño = "45"
    print(monitor1)

    monitor1.marca = "14"
    print(monitor1)


    monitor2 = Monitor_divc("Lanovo", "44 pulgadas")
    print(monitor2)
