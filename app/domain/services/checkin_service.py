from app.domain.entities.checkin import CheckIn
from app.domain.repositories.checkin_repository import CheckInRepository


class CheckInService:

    def __init__(self, repository: CheckInRepository):
        self.repository = repository

    def create(self, name: str, document: str | None) -> CheckIn:
        checkin = CheckIn(name, document)
        self.repository.save(checkin)
        return checkin

    def list_all(self) -> list[CheckIn]:
        return self.repository.list_all()
