from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/login", response_class=HTMLResponse)
def login_view(request: Request):
    return templates.TemplateResponse("login/login.html", {"request": request})

@router.post("/login")
def login_post(request: Request):
    # Por ahora redirige sin validar
    return RedirectResponse(url="/estudiante", status_code=302)
