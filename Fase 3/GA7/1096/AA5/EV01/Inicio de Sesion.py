from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Recibir los datos de usuario y contraseña de la petición POST
    username = request.form['username']
    password = request.form['password']
    
    # Conectarse a la base de datos
    conn = psycopg2.connect(<connection string>)
    cursor = conn.cursor()
    
    # Ejecutar un query para consultar el usuario y la contraseña en la tabla de usuarios
    cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    
    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()
    
    # Verificar si la contraseña es correcta
    if result and result[0] == password:
        # Devolver un mensaje de éxito
        return "Autenticación exitosa!", 200
    else:
        # Devolver un mensaje de error en la autenticación
        return "Error en la autenticación", 401
