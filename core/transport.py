import random
from loguru import logger
from utils.checksum import crc32_text
from models.transport_models import TransportSegment
from models.stats import TransportStats


class TransportLayer:
    """
    Simulates the Transport Layer (TCP-like behavior).
    - Splits data into segments
    - Simulates packet loss
    - Retransmits lost packets
    - Reassembles data on receive
    """

    def __init__(self, loss_probability: float = 0.15):
        self.loss_probability = loss_probability
        self.stats = TransportStats()

    def send(self, data: str):
        """
        Split data into fixed-size segments and simulate packet loss.
        """
        segments = []

        # Split into 10-character segments
        for i in range(0, len(data), 10):
            chunk = data[i:i + 10]
            segment = TransportSegment(
                seq=len(segments) + 1,
                port=random.randint(1024, 65535),
                checksum=crc32_text(chunk),
                payload=chunk
            )
            segments.append(segment)

        self.stats.total = len(segments)
        delivered_segments = []

        for seg in segments:
            # Simulate packet loss
            if random.random() < self.loss_probability:
                self.stats.lost += 1
                logger.warning(
                    f"[Transport] Segment {seg.seq} lost → retransmitting"
                )
                self.stats.retransmitted += 1

            delivered_segments.append(seg)

        self.stats.delivered = len(delivered_segments)
        logger.info(
            f"[Transport] Delivery complete "
            f"(sent={self.stats.total}, lost={self.stats.lost}, "
            f"retransmitted={self.stats.retransmitted})"
        )

        return delivered_segments

    def receive(self, segments):
        logger.info("[Transport] Reassembling segments")
        return "".join(seg.payload for seg in segments)
