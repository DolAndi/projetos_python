from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)


def criptografar(texto):
    return f.encrypt(texto.encode()).decode("utf-8") 

def decriptografar(cript):
    return f.decrypt(bytes(cript,"utf-8")).decode("utf-8") 


