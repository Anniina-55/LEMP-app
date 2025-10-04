
from flask import Flask, jsonify
import os
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'appuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'changeme')
DB_NAME = os.getenv('DB_NAME', 'appdb')


@app.get('/api/health')
def health():
    return {'status': 'ok'}

# new route for fetching server time from the MySQL database
@app.get('/api/time')
def get_time():
    """Fetch server time from MySQL database."""
    conn = None
    cur = None
    row = None
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci'
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW()")  # mysql komento hakee nykyisen ajan
        row = cur.fetchone()
    except Exception as e:
        return jsonify(error="Could not fetch time", details=str(e)), 500
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return jsonify(server_time=str(row[0]))
    
@app.get('/api/quote')
def get_quote():
    conn = None
    cur = None
    row = None
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
        cur = conn.cursor()
        cur.execute("SELECT quote_text FROM quotes ORDER BY RAND() LIMIT 1")
        row = cur.fetchone()
    except Exception as e:
        return jsonify(error="Could not fetch quote", details=str(e)), 500
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()

    return jsonify(quote=row[0])


@app.get('/api/message')
def index():
    """Simple endpoint that greets from DB."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cur = conn.cursor()
    cur.execute("SELECT 'Hello from MySQL via Flask!'")
    row = cur.fetchone()
    cur.close()
    conn.close()
    return jsonify(message=row[0])


if __name__ == '__main__':
    # Dev-only fallback
    app.run(host='0.0.0.0', port=8000, debug=True)

