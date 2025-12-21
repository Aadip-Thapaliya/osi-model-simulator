import zlib

def crc32_text(data: str) -> int:
    return zlib.crc32(data.encode("utf-8")) & 0xFFFFFFFF
