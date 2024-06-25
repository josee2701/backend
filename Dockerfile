# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos requeridos
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el código fuente
COPY . .

# Establece un argumento para el entorno
ARG ENV=production

# Expone el puerto 8000
EXPOSE 8000

# Comando para ejecutar dependiendo del entorno
CMD if [ "$ENV" = "development" ]; then python manage.py runserver 0.0.0.0:8000; else gunicorn --bind 0.0.0.0:8000 config.wsgi:application; fi
