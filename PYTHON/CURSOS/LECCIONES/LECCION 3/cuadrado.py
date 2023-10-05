from figuras import Figura_geo
from colores import Color_fig

class Cuadrado_fig(Figura_geo, Color_fig):
    def __init__(self, lado, color) -> None:
        Figura_geo.__init__(self, lado, lado)
        Color_fig.__init__(self, color)

    def calcular_area(self):
        return self.alto * self.ancho