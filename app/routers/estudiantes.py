from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/estudiante", response_class=HTMLResponse)
def estudiante_home(request: Request):
    return templates.TemplateResponse("estudiantes/estudiante_home.html", {"request": request})
