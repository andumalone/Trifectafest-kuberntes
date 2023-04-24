FROm python:3.9-slim-buster

WORKDIR /app

COPY Trifectafest-BE-Python /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "app.py"]