import os


def file_exists(file_name: str):
    import os
    """ Verificar si es un archivo y si este existe """
    return os.path.isfile(file_name)


def encode_b64(word: str) -> str:
    """ Codificar en base64 """
    from base64 import b64encode
    encoded_word = b64encode(word.encode('utf-8'))
    return encoded_word.decode('utf-8')


def decode_b64(encoded_word: str) -> str:
    """ Decodificar y regresar al estado original """
    from base64 import b64decode
    decoded_word = b64decode(encoded_word.encode('utf-8'))
    return decoded_word.decode('utf-8')


def hash_string(plain_pass: str) -> str:
    """ Codificar una cadena en sha256 y devolver en Hex """
    from hashlib import sha256
    sha_signature = sha256(plain_pass.encode()).hexdigest()
    return sha_signature


basedir = os.getcwd()
filename = 'pila.txt'

with open(filename, 'w') as file:
    list(map(lambda x: file.write(x + '\n'), ['julio', 'jair', 'de', 'alba', 'garay']))

if file_exists(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        lines_encoded64 = list(map(lambda x: encode_b64(x), lines))
        lines_encoded64_sha256 = list(map(lambda x: hash_string(x), lines_encoded64))

with open('colas.backup.txt', 'w') as file:
        lines_encoded64.reverse()
        lines_encoded64_sha256.reverse()
        print(lines_encoded64)
        print(lines_encoded64_sha256)
        list(map(lambda x, y: file.write(f'{x};{y}\n'), lines_encoded64, lines_encoded64_sha256))
        os.remove(filename)

with open('colas.backup.txt', 'r') as file:
    lines = file.read().splitlines()
    # Split elements of the list and save the base64 strings
    lines_encoded64 = [line.split(';')[0] for line in lines]
    lines_encoded64.reverse()

    # Split elements of the list and save the hashes
    lines_encoded64_sha256 = [line.split(';')[1] for line in lines]
    lines_encoded64_sha256.reverse()
    # Decode the base64
    lines_decoded64 = list(map(lambda x: decode_b64(x), lines_encoded64))

    #     Save the decoded elements in the origin order
with open('colas.backup.txt', 'w') as file:
    list(map(lambda x: file.write(f'{x}\n'), lines_decoded64))
# Create folder if it doesn't exist

if not os.path.exists('sha256'):
    os.mkdir('sha256')

# Saving hashes to file
filepath = f'{basedir}/sha256/'
with open(f'{filepath}hashes.txt', 'w')as file:
    print(lines_encoded64_sha256)
    list(map(lambda x: file.write(f'{x}\n'), lines_encoded64_sha256))

# Asignar permisos 555 al archivo
os.chmod(f'{filepath}hashes.txt', 0o555)
os.system(f'nano {filepath}hashes.txt')
