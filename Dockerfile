FROM amd64/python:3.7

# RUN mkdir -p /var/www/dockerize-python/anti-spoofing-app
# WORKDIR /var/www/dockerize-python/anti-spoofing-app

COPY . .
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "server.py"]