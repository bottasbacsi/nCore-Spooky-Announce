# 🎃 nCore Spooky Discord Announcer

A Discord WebSocket-alapú értesítő rendszer, amely valós időben figyeli a "Spooky" eseményeket és automatikusan küld értesítéseket Discord webhook-on keresztül.

## ✨ Főbb jellemzők

- **Valós idejű monitorozás**: WebSocket kapcsolaton keresztül figyeli az eseményeket
- **Discord integráció**: Automatikus értesítések képekkel együtt
- **Rugalmas újracsatlakozás**: Automatikusan helyreállítja a kapcsolatot megszakadás esetén
- **Vizuális visszajelzés**: Rich könyvtárral színes konzol kimenet
- **Időbélyegzés**: Minden értesítés pontos időponttal

## 🛠 Telepítés és beállítás

### Előfeltételek
```bash
pip install -r requirements.txt
```

### Konfiguráció
1. **Discord Webhook beállítása**:
   - Hozz létre egy webhook-ot a Discord szervereden
   - Cseréld le a `WEBHOOK_URL` változót a saját webhook URL-edre:

```python
WEBHOOK_URL = 'https://discord.com/api/webhooks/...'
```

## 🚀 Futtatás

```bash
python discord_announce.py
```

## 📋 Működés

1. **Kapcsolódás**: A bot csatlakozik a WebSocket szerverhez
2. **Figyelés**: Valós időben figyeli a "spooky" típusú üzeneteket
3. **Értesítés**: Amint érkezik új tök esemény:
   - Küld egy Discord üzenetet
   - Véletlenszerű halloweeni képet csatol
   - Időbélyeggel látja el
4. **Hibakezelés**: Kapcsolat megszakadása esetén automatikusan újrapróbálkozik

## 🎨 Értesítések típusai

- **Normál tök**: `"Új tök"`
- **Captchás tök**: `"Új captchás tök"`
---

*Ügyelj rá, hogy a Discord webhook URL-ed biztonságosan legyen tárolva és ne oszd meg nyilvánosan!*
