from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/test_diagnostico")
def test_diagnostico_view(request: Request):
    return templates.TemplateResponse("estudiantes/test_diagnostico.html", {"request": request})
# Vista para resolver el test
