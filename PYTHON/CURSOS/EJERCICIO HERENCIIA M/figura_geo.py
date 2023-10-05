class Figura_geo:
    def __init__(self, alto, ancho) -> None:
        self._alto = alto
        self._ancho = ancho
    
    def __str__(self) -> str:
        return f'Alto: {self._alto}, Ancho: {self._ancho}'

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        self._alto = alto
    
    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho