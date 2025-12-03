# Uporabimo uradno Python sliko
FROM python:3.12-slim

# Nastavi delovni direktorij
WORKDIR /app

RUN apt-get update && apt-get install -y \
    fonts-dejavu-core \
    fontconfig \
    && rm -rf /var/lib/apt/lists/*

# Kopiraj requirements.txt in namesti odvisnosti
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiraj vse datoteke aplikacije
COPY . .

# Nastavi okoljsko spremenljivko za port
ENV PORT=5000

# Odpri port
EXPOSE 5000

# Zaženi aplikacijo
CMD ["python", "app.py"]
