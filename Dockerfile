FROM python:3.11-slim
WORKDIR /opt/app
COPY . .
RUN pip install --upgrade pip && pip install fastapi uvicorn pydantic
CMD ["venv/bin/python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
