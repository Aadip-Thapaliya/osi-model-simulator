import uuid
from loguru import logger

class SessionLayer:
    def send(self, data: str) -> str:
        session_id = uuid.uuid4()
        logger.info("[Session] Session ID attached")
        return f"SESSION={session_id}||{data}"

    def receive(self, data: str) -> str:
        return data.split("||", 1)[1]
