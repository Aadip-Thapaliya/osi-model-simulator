from dataclasses import dataclass

@dataclass
class TransportStats:
    total: int = 0
    lost: int = 0
    retransmitted: int = 0
    delivered: int = 0
