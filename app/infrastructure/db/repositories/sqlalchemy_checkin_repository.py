from sqlalchemy.orm import Session
from app.domain.entities.checkin import CheckIn
from app.domain.repositories.checkin_repository import CheckInRepository
from app.infrastructure.db.models import CheckInModel


class SQLAlchemyCheckInRepository(CheckInRepository):

    def __init__(self, db: Session):
        self.db = db

    def save(self, checkin: CheckIn) -> None:
        model = CheckInModel(
            name=checkin.name,
            document=checkin.document
        )
        try:
            self.db.add(model)
            self.db.commit()
        except Exception:
            self.db.rollback()
            raise

    def list_all(self) -> list[CheckIn]:
        rows = self.db.query(CheckInModel).all()
        return [CheckIn(r.name, r.document) for r in rows]
