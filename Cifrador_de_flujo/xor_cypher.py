from bitarray import bitarray

from Cifrador_de_flujo.linear_feedback_shift_register import generate_key_faster


def string_to_binary(text):
    bitarray_object = bitarray()
    bitarray_object.frombytes(text.encode('utf-8'))
    return bitarray_object


def binary_to_string(bitarray_object):
    text = bitarray(bitarray_object).tobytes().decode('utf-8')
    return text


seed = [1] * 17
mensaje = "Este es mi primer cifrador de flujo"
key = generate_key_faster(seed, trinomial=[17, 3, 0])
print(f"Mensaje original: \n{mensaje}")
encoded = string_to_binary(mensaje)
print(f'Mensaje codificado en binario: \n{encoded}')
decoded = (binary_to_string(encoded))
print(f'Mensaje decodificado: \n{decoded}')

### Cifrado con LFSR ###
# Codificar en binario
encoded = bitarray(encoded)
key = bitarray(key)
dif = len(key) - len(encoded)

# Preparando para aplicar xor
print(f'\nkey: {len(key)} mensaje_binario: {len(encoded)}')
for i in range(dif):
    key.pop()
print(f'key: {len(key)} mensaje_binario: {len(encoded)}')

encrypted = (encoded ^ key)
print(f'\nMensaje cifrado con llave generada: \n{encrypted}')
decrypted = (encrypted ^ key)
print(f'Mensaje desencriptado pero codificado en binario: \n{decrypted}')
decoded = (binary_to_string(decrypted))
print(f'\nMensaje decodificado: \n{decoded}')
