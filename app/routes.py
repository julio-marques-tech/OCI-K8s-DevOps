from flask import Blueprint, request, jsonify
import psycopg2
import os

routes = Blueprint('routes', __name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/mydatabase")

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

@routes.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is running"}), 200

@routes.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(users)

@routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and Email are required'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", (name, email))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'id': user_id, 'name': name, 'email': email}), 201

