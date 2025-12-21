from dataclasses import dataclass

@dataclass
class TransportSegment:
    seq: int
    port: int
    checksum: int
    payload: str
