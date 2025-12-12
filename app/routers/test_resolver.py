from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/test_resolver")
def test_resolver_view(request: Request):
    return templates.TemplateResponse("estudiantes/test_resolver.html", {"request": request})
