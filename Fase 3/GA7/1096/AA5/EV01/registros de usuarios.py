from flask import Flask, request
import psycopg2

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Recibir los datos de usuario y contraseña de la petición POST
    username = request.form['username']
    password = request.form['password']
    
    # Conectarse a la base de datos
    conn = psycopg2.connect(<connection string>)
    cursor = conn.cursor()
    
    # Ejecutar un query para insertar el nuevo usuario y contraseña en la tabla de usuarios
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    
    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()
    
    # Devolver un mensaje de éxito
    return "Usuario registrado exitosamente!", 201