def file_exists(file_name: str):
    import os
    """ Verificar si es un archivo y si este existe """
    return os.path.isfile(file_name)


def get_file_content(filename: str, ):
    with open(filename, 'r+') as file:
        lines = file.read().splitlines()
    return lines


if not file_exists('pila.txt'):
    with open('pila.txt', 'w'):
        print('Creating <<pila.txt>> file..')

with open('pila.txt', 'a') as file:
    number_of_lines = int(input("Ingresar número de lineas: "))
    for i in range(number_of_lines):
        file.write(str(input(f"Ingresa algun dato para la linea {i + 1}: ") + '\n'))

print(get_file_content('pila.txt'))
