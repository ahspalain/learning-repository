from figura_geo import Figura_geo
from color import Color_fig

class Cuadrado_figu(Figura_geo, Color_fig):
    def __init__(self, lado, color) -> None:
        Figura_geo.__init__(self, lado, lado)
        Color_fig.__init__(self, color)
    
    def calc_areaC(self):
        return self._alto * self._ancho
    
    def __str__(self) -> str:
        return f'{Figura_geo.__str__(self)}, {Color_fig.__str__(self)}'
    