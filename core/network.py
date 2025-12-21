from loguru import logger


class NetworkLayer:
    def send(self, segments):
        logger.info("[Network] IP addresses attached (simulated)")
        return segments

    def receive(self, packets):
        return packets

