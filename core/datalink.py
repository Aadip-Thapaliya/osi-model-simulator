from loguru import logger


class DataLinkLayer:
    def send(self, packets):
        logger.info("[DataLink] MAC addresses added (simulated)")
        return packets

    def receive(self, frames):
        return frames
