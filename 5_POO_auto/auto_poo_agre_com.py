class Auto:
    def __init__(self, marca, cilindros, caballos, turbo, obj_faros=None):
        if obj_faros is None:
            obj_faros = Faros('', '')

        self.marca = marca
        self.cilindros = cilindros
        self.caballos = caballos
        self.turbo = turbo
        self.obj_motor = Motor(self.cilindros, self.caballos, self.turbo)
        self.obj_faros = obj_faros

    def __repr__(self):
        return f"{self.marca}, {self.obj_motor}, {self.obj_faros.tipo}"

    def turn_on(self):
        print("Encendido")

    def turn_off(self):
        print("Apagado")


class Motor:
    def __init__(self, cilindros, caballos, turbo):
        self.cilindros = cilindros
        self.caballos = caballos
        self.turbo = turbo

    def __repr__(self):
        return f"Motor de {self.cilindros} cilindros, {self.caballos} caballos, turbo: {self.turbo}"


class Faros:
    def __init__(self, tipo, color):
        self.tipo = tipo
        self.color = color


if __name__ == "__main__":
    obj_faros1 = Faros('LED', 'Blanco')
    obj_faros2 = Faros('Xenón', 'Blanco')
    obj_auto1 = Auto("ferrari", 12, 400, True)
    obj_auto2 = Auto("Nissan", 4, 100, False, obj_faros1)
    obj_auto3 = Auto("Mazda", 6, 250, True)
    obj_auto4 = Auto("Volkswagen", 4, 220, False, obj_faros2)
    obj_auto5 = Auto("Ford", 8, 200, False)

    print(obj_auto1)
    print(obj_auto1.obj_motor)
    print(obj_auto2)
