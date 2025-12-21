import base64

def encrypt(text: str, key: int = 7) -> str:
    return "".join(chr((ord(c) + key) % 0x110000) for c in text)

def decrypt(text: str, key: int = 7) -> str:
    return "".join(chr((ord(c) - key) % 0x110000) for c in text)

def encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()

def decode(text: str) -> str:
    return base64.b64decode(text.encode()).decode()
