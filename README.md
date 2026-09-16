# FastAPI + SQLModel Lifespan Example

A minimal FastAPI application demonstrating modern application lifecycle management with the `lifespan` context manager, combined with **SQLModel** for database table creation on startup.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-teal)
![SQLModel](https://img.shields.io/badge/SQLModel-ORM-red)

---

## 🇬🇧 English

### Overview
This project shows how to use FastAPI's `lifespan` context manager — the modern replacement for the deprecated `@app.on_event("startup")` / `@app.on_event("shutdown")` decorators — to run setup and teardown logic around the application's lifetime. On startup, it creates all database tables defined via SQLModel.

### Features
- Modern `lifespan` context manager for startup/shutdown logic
- SQLModel table definition and automatic table creation
- SQLite database configured via `create_engine`
- A simple root endpoint to verify the app is running

### Requirements
- Python 3.10 or higher
- `fastapi`
- `sqlmodel`
- `uvicorn`

### Installation
```bash
pip install fastapi sqlmodel uvicorn
```

### Usage
```bash
uvicorn fastapi_lifespan:app --reload
```

Then open `http://127.0.0.1:8000` in your browser, or visit `http://127.0.0.1:8000/docs` for the interactive API documentation.

### How it works
The `@asynccontextmanager`-decorated `lifespan` function runs `SQLModel.metadata.create_all(engine)` before the `yield` statement — this executes once, when the application starts, creating all tables for models like `Item`. Any code placed after `yield` runs on shutdown, making this the ideal place for cleanup logic such as closing database connections.

Note: This project was developed with AI assistance as part of my learning process

---

## 🇩🇪 Deutsch

### Überblick
Dieses Projekt zeigt, wie man den `lifespan`-Kontextmanager von FastAPI verwendet — den modernen Ersatz für die veralteten `@app.on_event("startup")` / `@app.on_event("shutdown")`-Decorators —, um Setup- und Teardown-Logik über die Lebensdauer der Anwendung hinweg auszuführen. Beim Start werden alle über SQLModel definierten Datenbanktabellen erstellt.

### Funktionen
- Moderner `lifespan`-Kontextmanager für Start-/Beendigungslogik
- SQLModel-Tabellendefinition und automatische Tabellenerstellung
- SQLite-Datenbank, konfiguriert über `create_engine`
- Ein einfacher Root-Endpunkt zur Überprüfung, ob die App läuft

### Voraussetzungen
- Python 3.10 oder höher
- `fastapi`
- `sqlmodel`
- `uvicorn`

### Installation
```bash
pip install fastapi sqlmodel uvicorn
```

### Verwendung
```bash
uvicorn fastapi_lifespan:app --reload
```

Öffne anschließend `http://127.0.0.1:8000` im Browser, oder besuche `http://127.0.0.1:8000/docs` für die interaktive API-Dokumentation.

### Funktionsweise
Die mit `@asynccontextmanager` versehene `lifespan`-Funktion führt `SQLModel.metadata.create_all(engine)` vor der `yield`-Anweisung aus — dies geschieht einmalig beim Start der Anwendung und erstellt alle Tabellen für Modelle wie `Item`. Jeglicher Code nach `yield` wird beim Herunterfahren ausgeführt, was diesen Bereich zum idealen Ort für Aufräumlogik wie das Schließen von Datenbankverbindungen macht.

Hinweis: Dieses Projekt wurde im Rahmen meines Lernprozesses mit KI-Unterstützung entwickelt

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu proje, FastAPI'nin `lifespan` context manager'ının nasıl kullanılacağını gösterir — kullanımdan kaldırılan `@app.on_event("startup")` / `@app.on_event("shutdown")` decorator'larının modern karşılığı — uygulamanın yaşam döngüsü boyunca kurulum ve kapanış mantığını çalıştırmak için. Uygulama başladığında, SQLModel üzerinden tanımlanan tüm veritabanı tabloları oluşturulur.

### Özellikler
- Başlangıç/kapanış mantığı için modern `lifespan` context manager
- SQLModel tablo tanımı ve otomatik tablo oluşturma
- `create_engine` ile yapılandırılmış SQLite veritabanı
- Uygulamanın çalıştığını doğrulamak için basit bir root endpoint

### Gereksinimler
- Python 3.10 veya üzeri
- `fastapi`
- `sqlmodel`
- `uvicorn`

### Kurulum
```bash
pip install fastapi sqlmodel uvicorn
```

### Kullanım
```bash
uvicorn fastapi_lifespan:app --reload
```

Ardından tarayıcında `http://127.0.0.1:8000` adresini aç, ya da interaktif API dokümantasyonu için `http://127.0.0.1:8000/docs` adresini ziyaret et.

### Nasıl çalışır?
`@asynccontextmanager` ile işaretlenmiş `lifespan` fonksiyonu, `yield` ifadesinden önce `SQLModel.metadata.create_all(engine)` komutunu çalıştırır — bu, uygulama başladığında bir kez çalışır ve `Item` gibi modeller için tüm tabloları oluşturur. `yield` sonrasına yerleştirilen herhangi bir kod, kapanış sırasında çalışır; bu da veritabanı bağlantılarını kapatmak gibi temizlik işlemleri için ideal bir yerdir.

Not: Bu proje öğrenme sürecimin bir parçası olarak yapay zeka desteğiyle geliştirilmiştir

