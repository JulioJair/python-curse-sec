class Auto:
    def __init__(self, marca=None, color=None, gas=None):
        self.marca = marca
        self.color = color
        self._gasolina = gasolina

    def avanzar(self, distancia, rel_gas_km=1 / 800):
        """Distancia en km"""
        print('Avanzando')
        gasolina_gastada = distancia * rel_gas_km
        self._gasolina -= gasolina_gastada

    def detener(self):
        print('Frenando')

    def get_nivel_gasolina(self):
        print(f"Nivel de gasolina: {self._gasolina * 100}%")

    def _llenar_tanque(self):
        if self._gasolina < 1:
            self._gasolina = 1
            print("Tanque llenado con éxito")
        else:
            print("El tanque ya está lleno al máximo de su capacidad!")



if __name__ == "__main__":
    a1 = Auto('Nissan', 'Gris', 16 / 16)
    a2 = Auto('Ferrari', 'rojo', 15 / 16)
    a3 = Auto('Mazda', 'Negro', 1 / 16)
    a4 = Auto('BMW', 'Azul', 14 / 16)
    a5 = Auto('Ford', 'Blanco', 10 / 16)
    a6 = Auto('Kia', 'Rojo', 5 / 16)

    print(a2)
    a2.get_nivel_gasolina()
    a2.avanzar(50)
    a2.get_nivel_gasolina()
    a2._llenar_tanque()
    a2.get_nivel_gasolina()
