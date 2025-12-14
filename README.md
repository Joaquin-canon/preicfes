# 🚀  Info

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- 🐍 [Python 3.10+](https://www.python.org/downloads/)
- 🐬 [MySQL Server](https://dev.mysql.com/downloads/mysql/)
- 📦 [pip](https://pip.pypa.io/en/stable/installation/) (gestor de paquetes de Python)
- 🌿 [Git](https://git-scm.com/) (para clonar el repositorio)

---

## 🛠️ Instrucciones de Instalación


#### 1. Clona el proyecto

```bash
 it clone https://github.com/Joaquin-canon/preicfes.git
```

#### 2. Entra en el directorio del proyecto

```bash
  cd preicfes

```

#### 3. Crea un entorno virtual `venv`

```bash
  python -m venv venv
```

#### 4. Activa el entorno virtual

(Windows)

```bash

  venv\Scripts\activate 

```
(Linux/Mac)
```bash

  source venv/bin/activate (Linux/Mac)
```


#### 4.1 *Opcional - Si pide permisos (Ejecutar antes del activate)



```bash
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Unrestricted
```

#### 5. Instala las dependencias necesarias

```bash
  pip install -r requirements.txt
```

#### 6. Inicia el servidor de desarrollo

```bash
  uvicorn main:app --reload
```
