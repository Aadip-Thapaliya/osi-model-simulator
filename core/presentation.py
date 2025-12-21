from loguru import logger
from utils.crypto import encrypt, decrypt, encode, decode

class PresentationLayer:
    def send(self, data: str) -> str:
        encrypted = encrypt(data)
        encoded = encode(encrypted)
        logger.info("[Presentation] Data encrypted and encoded")
        return encoded

    def receive(self, data: str) -> str:
        decoded = decode(data)
        decrypted = decrypt(decoded)
        logger.info("[Presentation] Data decoded and decrypted")
        return decrypted
