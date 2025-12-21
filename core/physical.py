from loguru import logger
from utils.binary import to_binary, from_binary


class PhysicalLayer:
    """
    Simulates the Physical Layer.
    Converts payload data to binary and back without
    destroying higher-layer structure.
    """

    def send(self, frames):
        logger.info("[Physical] Converting payloads to binary")
        binary_frames = []

        for frame in frames:
            # frame is a TransportSegment
            binary_payload = to_binary(frame.payload)
            binary_frames.append((frame, binary_payload))

        return binary_frames

    def receive(self, binary_frames):
        logger.info("[Physical] Converting binary to payloads")
        restored_frames = []

        for frame, binary_payload in binary_frames:
            restored_payload = from_binary(binary_payload)
            frame.payload = restored_payload
            restored_frames.append(frame)

        return restored_frames
