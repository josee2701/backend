# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos requeridos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el código fuente
COPY . .

# Comando temporal para verificar las variables de entorno
RUN env

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
