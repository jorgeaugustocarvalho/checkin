from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.infrastructure.db.session import get_db
from app.infrastructure.db.repositories.sqlalchemy_checkin_repository import (
     SQLAlchemyCheckInRepository
)
from app.domain.services.checkin_service import CheckInService
from app.application.use_cases.create_checkin import CreateCheckInUseCase

router = APIRouter()

templates = Jinja2Templates(directory="app/infrastructure/web/templates")


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    repo = SQLAlchemyCheckInRepository(db)
    service = CheckInService(repo)
    checkins = service.list_all()
    return templates.TemplateResponse("index.html", {"request": request, "checkins": checkins})


@router.post("/checkin")
def create_checkin(
        name: str = Form(...),
        document: str | None = Form(None),
        db: Session = Depends(get_db)
):
    repo = SQLAlchemyCheckInRepository(db)
    service = CheckInService(repo)
    use_case = CreateCheckInUseCase(service)

    use_case.execute(name, document)

    return RedirectResponse("/", status_code=303)
