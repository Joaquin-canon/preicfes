from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Login
from app.routers.login import router as login_router   
from fastapi.responses import HTMLResponse, RedirectResponse

# Estudiantes
from app.routers.estudiantes import router as estudiantes_router
from app.routers.dashboard import router as dashboard_router
from app.routers.test_diagnostico import router as test_diag_router
from app.routers.test_resolver import router as test_resolver_router

app = FastAPI()

# Archivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Registrar routers
app.include_router(login_router)
app.include_router(estudiantes_router)
app.include_router(dashboard_router)
app.include_router(test_diag_router)
app.include_router(test_resolver_router)

# Ruta raíz
@app.get("/")
def root():
    return RedirectResponse(url="/login")
