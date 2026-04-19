# Proyecto 03 - Aplicacion Multicontenedor con Docker Compose
**Asignatura:** Infraestructura y Seguridad Computacional
**Universidad de Ibague - Ingenieria de Sistemas**
**Docente:** Msc. Ing. Carlos Andres Diaz Santacruz

## Descripción
Aplicación web multicontenedor desplegada con Docker Compose. El stack esta compuesto por tres servicios:

- **web**: API en Python (Flask) que consulta el estado de la base de datos.
- **db**: Servidor PostgreSQL 15 persistente mediante volumen.
- **adminer**: Interfaz web para visualizar y administrar la base de datos.

## Requisitos
- Docker 24+ con Docker Compose v2 (plugin integrado)
- Sistema Linux o WSL2

## Como ejecutar
​```bash
docker compose up -d --build
​```

Servicios disponibles:

- API Flask: http://localhost:5000
- Adminer: http://localhost:8080 (System: PostgreSQL, Server: db, User: appuser, Password: apppassword, DB: appdb)

## Detener y limpiar
​```bash
docker compose down            # detiene los contenedores
docker compose down -v         # detiene y borra los volumenes
​```

## Imagen publicada en Docker Hub
`rosedev1/fullstack-app:latest`