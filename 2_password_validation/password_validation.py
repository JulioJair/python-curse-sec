import re


def password_validation(user_entry):
    """
    Validate the user_entry password
    If flag is_okay remains True, the password is valid.
    """
    is_okay = True
    if len(user_entry) != 8:
        is_okay = False
        print("Debe tener 8 caracteres")

    if user_entry.count("b") < 2:
        is_okay = False
        print("Debe tener al menos dos caracteres iguales a 'b'")

    if user_entry.count("k") == 2:
        is_okay = False
        print("No debe tener dos caracteres iguales a 'k")

    if not re.search('[*+%$]', user_entry):
        is_okay = False
        print("Debe tener al menos un '*' o '+' o '%' o '$'")

    return is_okay


def request_password() -> bool:
    user_entry = input("Ingresa password: ")
    if password_validation(user_entry):
        print("Acceso Concedido")
        return True
    return False


# Request the password until the user write a valid password.
while True:
    if request_password():
        break
