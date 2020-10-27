import os


def file_exists(file_name: str):
    """ Verificar si es un archivo y si este existe """
    return os.path.isfile(file_name)

    # if not file_exists('pila.txt'):


def show_content(filename: str):
    with open(filename, 'r+') as file:
        for line in file:
            print(line)
    return None


with open('pila.txt', 'w') as f:
    number_of_lines = int(input("Ingresar número de lineas: "))
    for i in range(number_of_lines):
        f.write(str(input(f"Ingresa algun dato para la linea {i + 1}: ") + '\n'))

show_content('pila.txt')
