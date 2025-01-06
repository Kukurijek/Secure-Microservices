# Basis-Image verwenden
FROM python:3.11-slim

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Abhängigkeiten kopieren und installieren
COPY packages.txt .
RUN pip install --no-cache-dir -r packages.txt

# Anwendungscode kopieren
COPY main.py .

# Container starten mit Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
