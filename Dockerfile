FROM python:3.11-slim

WORKDIR /app

RUN useradd -m appuser

COPY app.py .

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "app.py"]