class Cifrado_XOR(object):

    def __init__(self, key=0):
        self.__key = key

    def encrypt(self, content, key):

        # pre-condición
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        # Esta lista sera retornada
        ans = []

        for ch in content:
            ans.append(chr(ord(ch) ^ key))

        return ans

    def decrypt(self, content, key):

        # pre-condición
        assert (isinstance(key, int) and isinstance(content, list))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        # This will be returned
        ans = []

        for ch in content:
            ans.append(chr(ord(ch) ^ key))

        return ans

    def encrypt_string(self, content, key=0):
        # Encriptar cadenas de texto
        # pre-condición
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def decrypt_string(self, content, key=0):
        # Descifrar

        # pre-condición
        assert (isinstance(key, int) and isinstance(content, str))

        key = key or self.__key or 1

        while (key > 255):
            key -= 255

        ans = ""

        for ch in content:
            ans += chr(ord(ch) ^ key)

        return ans

    def encrypt_file(self, file, key=0):
        # Cifrar archivos de texto

        # pre-condición
        assert (isinstance(file, str) and isinstance(key, int))

        try:
            with open(file, "r") as fin:
                with open("encrypt.out", "w+") as fout:
                    for line in fin:
                        fout.write(self.encrypt_string(line, key))

        except:
            return False

        return True

    def decrypt_file(self, file, key):
        # Descifrar archivo de texto

        # pre-condición
        assert (isinstance(file, str) and isinstance(key, int))

        try:
            with open(file, "r") as fin:
                with open("decrypt.out", "w+") as fout:
                    for line in fin:
                        fout.write(self.decrypt_string(line, key))

        except:
            return False

        return True


crypt = Cifrado_XOR()
key = 34

encr = crypt.encrypt_string(input("Ingresa la palabra"), key)
decr = crypt.decrypt_string(encr, key)

print("Cifrado: %s" % encr)
print("Descifrado: %s" % decr)
