import subprocess
import datetime

# Ruta del repositorio local
repo_path = r"C:/Users/soportetecnico02/OneDrive - misena.edu.co/BD/ADSO"

# Comando para hacer un pull de la rama actual
subprocess.call([r"C:\Program Files\Git\bin\git.exe", 'pull'], cwd=repo_path)

# Comando para agregar todos los archivos al staging area
subprocess.call([r"C:\Program Files\Git\bin\git.exe", 'add', '-A'], cwd=repo_path)

# Comando para configurar el autocrlf
subprocess.call([r"C:\Program Files\Git\bin\git.exe", 'config', '--global', 'core.autocrlf', 'true'], cwd=repo_path)

# Comando para agregar los cambios al staging area
subprocess.call([r"C:\Program Files\Git\bin\git.exe", 'add', '-A'], cwd=repo_path)

# Comando para hacer un commit con la fecha y hora actual
commit_message = 'Update "{}"'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
subprocess.call([r"C:\Program Files\Git\bin\git.exe", 'commit', '-m', commit_message], cwd=repo_path)

# Comando para hacer un push de los cambios al repositorio remoto
subprocess.call([r"C:\Program Files\Git\bin\git.exe", 'push'], cwd=repo_path)
