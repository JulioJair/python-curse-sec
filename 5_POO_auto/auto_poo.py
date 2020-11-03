class Auto:
    def __init__(self, marca=None, color=None, gas=None):
        self.marca = marca
        self.color = color
        self._gasolina = gas

    def avanzar(self):
        print('Avanzando')

    def detener(self):
        print('Frenando')

    def get_nivel_gasolina(self):
        print(self._gasolina)


a1=Auto('Nissan','Gris','Lleno')
a2=Auto('Ferrari','rojo','Lleno')
a3=Auto('Mazda','Negro','Bajo')
a4=Auto('BMW','Azul','Alto')
a5=Auto('Ford','Blanco','Bajo')
a6=Auto('Kia','Rojo','Vacío')

a6.get_nivel_gasolina()