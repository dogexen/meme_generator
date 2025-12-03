# Meme Generator

Preprost spletni generator memov, razvit z Flask in Pillow, dockeriziran za enostavno uporabo.

## Funkcionalnosti
- Nalaganje slik preko spletnega vmesnika
- Dodajanje zgornjega in spodnjega teksta
- Avtomatsko generiranje mema z belim tekstom in črno obrobo
- Prenos generiranega mema

## Tehnologije
- Python 3.12
- Flask 3.0.0
- Pillow 10.1.0
- Docker

## Zagon z Dockerjem

### Gradnja slike:
```bash
docker build -t meme-generator .
```

### Zagon kontejnerja:
```bash
docker run -p 5000:5000 meme-generator
```

### Odprite v brskalniku:
http://localhost:5000

## Struktura projekta
```
meme-generator/
├── app.py              # Glavna Flask aplikacija
├── requirements.txt    # Python odvisnosti
├── Dockerfile         # Docker konfiguracija
├── templates/
│   └── index.html     # Spletni vmesnik
├── static/
│   └── uploads/       # Mapa za naložene slike
└── README.md          # Ta dokument
```

## Avtor
Gašper Potočnik

## Licenca
MIT
