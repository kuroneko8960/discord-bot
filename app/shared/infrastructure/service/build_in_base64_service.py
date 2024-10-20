import base64

from app.shared.infrastructure.service.base64_service_interface import Base64ServiceInterface


class BuildInBase64Service(Base64ServiceInterface):
    def encode(self, value: str) -> str:
        return base64.urlsafe_b64encode(value.encode()).decode('ascii')