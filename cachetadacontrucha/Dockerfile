# Usamos una imagen base ligera de Python 3.9
FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el archivo de requerimientos y los instalamos
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente de la aplicación al contenedor
COPY . .

EXPOSE 9090

# Comando para correr la aplicación
CMD ["python", "main.py"]
