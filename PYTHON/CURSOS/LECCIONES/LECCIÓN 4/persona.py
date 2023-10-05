class Persona:

    contador_personas = 0

    def __init__(self, nombre, edad) -> None:
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        return f'Persona {self.id_persona}, Nombre: {self.nombre}, Edad: {self.edad}'

persona1 = Persona("Juan", 28)
print(persona1)

persona2 = Persona("María", 24)
print(persona2)