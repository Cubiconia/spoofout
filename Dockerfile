FROM amd64/python:3.8

# RUN mkdir -p /var/www/dockerize-python/anti-spoofing-app
# WORKDIR /var/www/dockerize-python/anti-spoofing-app

COPY . .
RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "server.py"]