FROM python:3.11-slim

WORKDIR /app

COPY translate_worker.py .

RUN pip install requests

CMD ["python", "translate_worker.py"]
