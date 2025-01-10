# 📡 Real-time Log to Telegram Bot

This project monitors a log file in real-time and sends specified content to a Telegram chat. It's designed to be configurable and adaptable to various log formats, making it a versatile tool for notifications. 🚀

---

## ✨ Features
- **Real-time Monitoring**: 📜 Watches a log file for updates using `watchdog`.
- **Telegram Integration**: 🤖 Sends formatted messages to a Telegram bot.
- **Configurable**: ⚙️ Easily adjust the title, start and end keywords, and log file path.
- **Efficient**: 🛡️ Ensures no duplicate messages are sent if the log content hasn't changed.

---

## ✅ Prerequisites
- 🐍 Python 3
- Telegram Bot Token ([Create a Telegram Bot](https://core.telegram.org/bots#botfather))
- Chat ID of the recipient ([Find your Chat ID](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id))

---

## ⚙️ Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/RealTimeLog-to-Telegram.git
   cd RealTimeLog-to-Telegram
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Running Bot with log**
   ```bash
   python3 bot.py | tee output.log
   ```


---

## 🛠️ Configuration

Edit the configuration section at the top of `log_to_telegram.py`:

```python
# Path to the log file
log_file_path = "output.log"

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN = "<YOUR_BOT_TOKEN>"
TELEGRAM_CHAT_ID = "<YOUR_CHAT_ID>"

# Log Configuration
CONFIG = {
    "title": "Process Summary",
    "keyword_from": "Account",
    "keyword_end": "App ID"
}
```

- **log_file_path**: 📂 Path to the log file to monitor.
- **TELEGRAM_BOT_TOKEN**: 🔑 Token of your Telegram bot.
- **TELEGRAM_CHAT_ID**: 💬 Chat ID where messages will be sent.
- **CONFIG**:
  - `title`: 🏷️ Title of the message.
  - `keyword_from`: 🔍 Start keyword to extract log content.
  - `keyword_end`: 🛑 End keyword to stop extraction.

---

## ▶️ Usage

Run the script:
```bash
python log_to_telegram.py
```

The script will:
1. 📡 Monitor the specified log file.
2. 📤 Extract content between `keyword_from` and `keyword_end`.
3. 📨 Send the content to your Telegram chat.

---

## 📝 Example

### Input Log
```
[✓] Account: email@gmail.com
[✓] Points: 15215
[✓] Social: 3/3 verified
[✓] Keepalive: Active
[✓] Proxy: protocol://ip:port
[✓] App ID: 6769d3d1asfa9d4c75882ecd5
```

### Config
```python
CONFIG = {
    "title": "Process Summary",
    "keyword_from": "Account",
    "keyword_end": "App ID"
}
```

### Telegram Output
```
[Process Summary]
[✓] Account: email@gmail.com
[✓] Points: 15215
[✓] Social: 3/3 verified
[✓] Keepalive: Active
[✓] Proxy: protocol://ip:port
[✓] App ID: 6769d3d1asfa9d4c75882ecd5
```

---

## 🤝 Contributing

Feel free to submit issues or pull requests if you find bugs or have feature suggestions! 🌟

---

