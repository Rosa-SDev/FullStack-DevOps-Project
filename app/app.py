from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

# Variables de entorno para conectarse a la base de datos
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "apppassword")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_connection():
    """Abre una conexion a PostgreSQL usando las variables de entorno."""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
    )


@app.route("/")
def home():
    """Endpoint principal: verifica conexion a la base de datos."""
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({
            "message": "Aplicacion desplegada correctamente con Docker y Docker Compose",
            "database": "PostgreSQL conectado",
            "version": version,
            "autor": "Rosa - Proyecto 03 Infraestructura y Seguridad Computacional"
        })
    except Exception as e:
        return jsonify({
            "message": "Aplicacion funcionando, pero sin conexion a la base de datos",
            "error": str(e)
        }), 500


@app.route("/health")
def health():
    """Endpoint de salud para pruebas rapidas."""
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)