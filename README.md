# 📦 Orders Service API - Proyecto Final Integrador

Este repositorio contiene el **Proyecto Final Integrador** desarrollado como culminación de la capacitación avanzada en "Python + IA". 

El proyecto consiste en un microservicio de gestión de órdenes logísticas construido bajo los principios de la **Arquitectura Limpia (Clean Architecture)** y **Puertos y Adaptadores (Arquitectura Hexagonal)**. Su diseño garantiza que las reglas de negocio base (Dominio) estén matemáticamente aisladas de los detalles de infraestructura (bases de datos, frameworks web y APIs externas).

## ✨ Características Principales

* **Arquitectura Hexagonal:** Separación estricta en capas (Dominio, Aplicación e Infraestructura) empleando Inyección de Dependencias y Protocolos (`typing.Protocol`).
* **API RESTful de Alto Rendimiento:** Frontera web asíncrona implementada con **FastAPI**.
* **Validación Estricta:** Uso de **Pydantic** para validar entradas/salidas (DTOs) en la frontera web y `dataclasses` para las entidades puras del dominio.
* **Persistencia Robusta:** Integración de **SQLAlchemy 2.0** con el patrón Repository y Unit of Work (UoW) para garantizar la integridad transaccional (ACID).
* **Migraciones de Esquema:** Control de versiones de la base de datos automatizado con **Alembic**.
* **Seguridad (Stateless):** Autenticación mediante **JSON Web Tokens (JWT)** para proteger los endpoints.
* **Calidad y Tipado Estricto:** Código auditado estáticamente por **Mypy** (modo estricto) y formateado/analizado con **Ruff** y **Black**.
* **Pruebas Automatizadas:** Suite de pruebas unitarias y de integración end-to-end (E2E) con **pytest**.
* **Containerización Segura:** Despliegue empaquetado en un contenedor **Docker Multistage** ejecutado sin privilegios de root (Hardening).
* **Integración Continua (CI/CD):** Pipeline configurado en **GitHub Actions** para ejecutar pruebas, análisis estático y auditorías de seguridad (`pip-audit`) en cada commit.

## 🛠️ Pila Tecnológica (Tech Stack)

* **Lenguaje:** Python 3.12+
* **Gestor de Dependencias:** Poetry
* **Web Framework:** FastAPI & Uvicorn
* **ORM & BD:** SQLAlchemy, Alembic, SQLite (Desarrollo)
* **Seguridad:** PyJWT, passlib
* **Calidad y Testing:** Pytest, Mypy, Ruff, pip-audit
* **Infraestructura:** Docker, GitHub Actions

## 📂 Estructura del Proyecto

```text
proyecto_final_orders/
├── src/
│   └── proyecto_final_orders/
│       ├── domain/               # Entidades puras (Dataclasses)
│       ├── application/          # Casos de uso y Puertos (Interfaces/Protocols)
│       ├── infrastructure/       # Adaptadores (FastAPI, SQLAlchemy, Seguridad)
│       └── main.py               # Entrypoint y Wiring (Inyección de dependencias)
├── tests/                        # Pruebas automatizadas (Pytest)
├── migraciones/                  # Scripts de Alembic para la BD
├── Dockerfile                    # Receta de construcción Multistage
├── pyproject.toml                # Configuración de dependencias (Poetry)
└── README.md                     # Documentación del proyecto
```

## 🚀 Guía de Instalación y Ejecución (Desarrollo Local)

### 1. Requisitos Previos
Asegúrate de tener instalados:
* [Python 3.12](https://www.python.org/downloads/)
* [Poetry](https://python-poetry.org/docs/#installation)
* [Docker](https://www.docker.com/) (Opcional, para la imagen de producción)

### 2. Clonar e Instalar Dependencias
```bash
git clone https://github.com/tu-usuario/proyecto_final_orders.git
cd proyecto_final_orders
poetry install
```

### 3. Ejecutar Migraciones de Base de Datos
Genera el archivo local SQLite (`orders.db`) con las tablas correspondientes:
```bash
poetry run alembic upgrade head
```

### 4. Levantar el Servidor de Desarrollo
```bash
poetry run uvicorn proyecto_final_orders.main:app --reload --app-dir src
```
El servidor estará corriendo en `http://127.0.0.1:8000`.

## 📖 Uso de la API (Swagger UI)

FastAPI genera documentación interactiva automáticamente.
1. Visita [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) en tu navegador.
2. Haz clic en el botón **Authorize** en la parte superior derecha.
3. Ingresa las credenciales de prueba (`username`: **admin**, `password`: **secreto**) para generar tu token JWT.
4. Interactúa con el endpoint protegido `POST /orders/` inyectando un payload JSON (ej. lista de artículos con `product_id`, `quantity` y `unit_price`).

## 🧪 Pruebas y Calidad de Código

Para garantizar la fiabilidad del sistema, ejecuta la suite de herramientas configuradas:

**Pruebas End-to-End:**
```bash
poetry run pytest -v
```

**Análisis Estricto de Tipos (Mypy):**
```bash
poetry run mypy src/
```

**Linter y Formateo (Ruff):**
```bash
poetry run ruff check .
```

**Auditoría de Vulnerabilidades en Dependencias:**
```bash
poetry run pip-audit --ignore-vuln PYSEC-2026-3740
```
*(Nota: Se excluye explícitamente una vulnerabilidad de NLTK documentada como excepción técnica).*

## 🐳 Despliegue en Producción (Docker)

El proyecto incluye un `Dockerfile` multistage optimizado para reducir el tamaño de la imagen y aislar los permisos de ejecución (Rootless).

**1. Construir la imagen:**
```bash
docker build -t orders-service:v1 .
```

**2. Ejecutar el contenedor:**
```bash
docker run -d -p 8000:8000 orders-service:v1
```