from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']

    conn = psycopg2.connect(
        host="hostname",
        database="dbname",
        user="username",
        password="password"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE user=%s AND password=%s", (user, password))

    if cur.rowcount == 1:
        return "Autenticación exitosa"
    else:
        return "Error en la autenticación"

if __name__ == '__main__':
    app.run()
