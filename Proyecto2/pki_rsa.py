class Pki_rsa:
    def __init__(self):
        from rsa import key
        (pub_key, priv_key) = key.newkeys(512)
        self.pub_key = pub_key
        self.__priv_key = priv_key

    def gen_keys(self):
        """Generate new keys for user, maybe in case of lost"""
        from rsa import key
        (pub_key, priv_key) = key.newkeys(512)
        self.pub_key = pub_key
        self.priv_key = priv_key

    def encrypt(self, message, pub_key_receiver):
        """Encrypt with the recipient public key"""
        from rsa import encrypt
        encoded_message = message.encode()
        encrypted_message = encrypt(encoded_message, pub_key_receiver)
        return encrypted_message

    def decrypt(self, encrypted_message):
        """Decrypt with personal private key"""
        from rsa import decrypt
        encoded_message = decrypt(encrypted_message, self.__priv_key)
        message = encoded_message.decode()
        return message


if __name__ == '__main__':
    # Se generan las claves al instanciar objetos
    persona1 = Pki_rsa()
    persona2 = Pki_rsa()
    print(f'Persona 1: {persona1.pub_key}')
    print(f'Persona 2: {persona2.pub_key}')

    # Persona 1 escribe un mensaje, lo cifra con la clave pública del destinatario y se lo envía
    mensaje1 = '\nTe veo a las 20:00 dónde siempre.'
    mensaje1_cifrado = persona1.encrypt(mensaje1, persona2.pub_key)
    mensaje1 = 'Destruido'

    # Persona 2 Recibe el mensaje cifrado y lo descifra con su clave privada
    mensaje1 = persona2.decrypt(mensaje1_cifrado)
    print(mensaje1)
    mensaje2 = '\nok'
    # Persona 2 añade texto a la conversación la cifra con la clave pública del destinatario y se lo envía
    mensaje1y2 = mensaje1 + mensaje2
    mensaje1y2_cifrado = persona2.encrypt(mensaje1y2, persona1.pub_key)
    mensaje1y2 = 'Destruido'

    # Persona 1 recibe la conversación cifrada y la descifra con su clave privada
    mensaje1y2 = persona1.decrypt(mensaje1y2_cifrado)
    print(mensaje1y2)