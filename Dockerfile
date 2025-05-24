FROM python:3.11-slim

RUN useradd -m appuser

WORKDIR /app
COPY . .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

CMD ["python", "server.py"]
