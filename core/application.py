from loguru import logger

class ApplicationLayer:
    def send(self, message: str) -> str:
        payload = (
            "POST /send-message HTTP/1.1\n"
            "Host: chat.example.com\n"
            "Content-Type: text/plain\n"
            f"Content-Length: {len(message)}\n\n"
            f"{message}"
        )
        logger.info("[Application] HTTP message created")
        return payload

    def receive(self, data: str) -> str:
        return data.split("\n\n", 1)[1]
