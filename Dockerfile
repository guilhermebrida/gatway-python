FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y libpq-dev python3-tk && rm -rf /var/lib/apt/lists/* 

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . .

RUN pip install poetry

RUN poetry install --no-root --no-dev

ENV POSTGRES_HOST=postgres
ENV POSTGRES_PORT=5432
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=postgres

CMD ["poetry", "run", "python", "-u", "./app/FOTA.py"]
# CMD ["python", "-u","./app/FOTA.py"]











