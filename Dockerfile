FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m venv venv
RUN /bin/bash -c "source venv/bin/activate"

CMD ["python", "main.py"]
