from cryptography.fernet import Fernet

class Encriptador:
    def __init__(self, secret_key=None):
        """
        Inicializa el encriptador con una clave secreta. Si no se proporciona,
        genera una nueva clave secreta.
        :param secret_key: Clave secreta como un string en formato base64.
        """
        if secret_key:
            self.fernet = Fernet(secret_key)
        else:
            # Genera una nueva clave secreta si no se proporciona
            self.secret_key = Fernet.generate_key()
            self.fernet = Fernet(self.secret_key)

    def encriptar(self, string):
        """
        Encripta un string.
        :param string: El string a encriptar.
        :return: String encriptado en formato base64.
        """
        return self.fernet.encrypt(string.encode('utf-8')).decode('utf-8')

    def desencriptar(self, token):
        """
        Desencripta un string encriptado.
        :param token: El string encriptado en formato base64.
        :return: El string desencriptado.
        """
        return self.fernet.decrypt(token.encode('utf-8')).decode('utf-8')

    def get_secret_key(self):
        """
        Devuelve la clave secreta utilizada para la encriptación.
        :return: Clave secreta en formato base64.
        """
        return self.secret_key.decode('utf-8')