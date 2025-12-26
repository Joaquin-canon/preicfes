# 📘 PreICFES

Plataforma web para la **preparación del examen ICFES Saber 11**, desarrollada con **FastAPI**, enfocada en la gestión académica por áreas, módulos de estudio y evaluaciones diagnósticas.

El sistema está diseñado con una arquitectura modular que permite escalar el contenido académico y los procesos de evaluación de forma organizada.

---

## 🚀 Tecnologías utilizadas

- **Python 3.11+**
- **FastAPI**
- **Uvicorn**
- **Jinja2** (templates HTML)
- **HTML / CSS / TailwindCSS** (migración progresiva)
- **SQLAlchemy**
- **MySQL** (en integración)

---

## 📂 Estructura del proyecto

```
preicfes/
├── app/
│   ├── main.py              # Punto de entrada FastAPI
│   ├── core/                # Configuración y utilidades
│   ├── routers/             # Rutas (endpoints)
│   │   └── admin/
│   │       └── catalogo.py  # Catálogo, áreas y tests
│   ├── models/              # Modelos de base de datos
│   ├── templates/           # Templates HTML (Jinja2)
│   │   ├── layout/
│   │   └── admin/
│   │       └── catalogo/
│   └── static/              # Archivos estáticos (CSS, JS)
├── venv/                    # Entorno virtual (NO se sube a GitHub)
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Joaquin-canon/preicfes.git
cd preicfes
```

---

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv venv
.\venv\Scripts\activate   # Windows
```

---

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecutar el proyecto

Desde la carpeta raíz del proyecto:

```bash
uvicorn app.main:app --reload
```

Abrir en el navegador:

```
http://127.0.0.1:8000
```

---

## 🧭 Funcionalidades actuales

- ✅ Catálogo de contenidos académicos
- ✅ Gestión de áreas ICFES:
  - RM – Razonamiento matemático
  - LC – Lectura crítica
  - CN – Ciencias naturales
  - EN – Inglés
  - CC – Competencias ciudadanas
- ✅ Gestión de módulos de estudio por área
- ✅ Tests especiales:
  - Test diagnóstico breve
  - Test socio-ocupacional
- 🚧 Banco de preguntas (en desarrollo)
- 🚧 Seguimiento de progreso académico

---

## 📌 Convenciones importantes

- El entorno virtual **`venv/` no se sube a GitHub**
- Los templates HTML van **solo en `app/templates/`**
- Los archivos CSS y JS van **solo en `app/static/`**
- El proyecto se ejecuta siempre con:

```bash
uvicorn app.main:app --reload
```

---

## 🛠️ Próximas mejoras

- 📚 Banco de preguntas por área
- 📊 Métricas y resultados por estudiante
- 🔐 Autenticación y gestión de roles
- 🧠 Recomendaciones de estudio
- 📈 Visualización de progreso académico

---

## 👨‍💻 Autor
 SENA Tecnoparque 
 co Autor
**Joaquín Canon**  
Proyecto académico y educativo

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.
