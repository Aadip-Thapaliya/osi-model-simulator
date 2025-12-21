def to_binary(text: str) -> str:
    return " ".join(format(b, "08b") for b in text.encode())

def from_binary(binary: str) -> str:
    return bytes(int(b, 2) for b in binary.split()).decode()
