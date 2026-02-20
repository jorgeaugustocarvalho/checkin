from abc import ABC, abstractmethod
from app.domain.entities.checkin import CheckIn


class CheckInRepository(ABC):
    """Abstract base for persisting and retrieving CheckIn entities.

    Methods:
    - save(checkin: CheckIn) -> None: Persist a single CheckIn instance.
    - list_all() -> list[CheckIn]: Return all stored CheckIn records in insertion or repository-defined order.
    """

    @abstractmethod
    def save(self, checkin: CheckIn) -> None:
        pass

    @abstractmethod
    def list_all(self) -> list[CheckIn]:
        pass