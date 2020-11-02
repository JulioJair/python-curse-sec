def file_exists_and_not_empty(filename):
    import os
    """ Verificar si es un archivo, si este existe y si no esta vacío"""
    return os.path.isfile(filename) and os.path.getsize(filename) > 0


def delete_first_line(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        lines = lines[:-1]
        print(lines)
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    return None


filename = 'pila.txt'
while True:
    if file_exists_and_not_empty(filename):
        option = input('Eliminar (e) Salir (s): ')
        option = option.casefold()
        if option == 'e' or option == 'eliminar':
            delete_first_line(filename)
        elif option == 's' or option == 'salir':
            break
        else:
            print('Opción inválida')

    else:
        print('Archivo vacío')
        break
