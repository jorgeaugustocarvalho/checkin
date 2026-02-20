from app.domain.services.checkin_service import CheckInService
from app.domain.entities.checkin import CheckIn


class CreateCheckInUseCase:

    def __init__(self, service: CheckInService):
        self.service = service

    def execute(self, name: str, document: str | None) -> CheckIn:
        return self.service.create(name, document)
