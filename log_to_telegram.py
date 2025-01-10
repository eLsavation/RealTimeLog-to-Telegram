import time
import re
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==================== KONFIGURASI ====================
# Path ke file log
log_file_path = "output.log"

# Konfigurasi bot Telegram
TELEGRAM_BOT_TOKEN = "Insert Telegram Token Here"
TELEGRAM_CHAT_ID = "Insert Telegram Chat ID Here"

# Konfigurasi log
CONFIG = {
    "title": "MONITOR",
    "keyword_from": "Account",
    "keyword_end": "App ID"
}
# =====================================================

# Fungsi untuk mengirim pesan ke Telegram
def send_telegram_message(title, content):
    message = f"[{title}]\n{content}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Event handler untuk perubahan file
class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.last_position = 0
        self.last_sent_log = None

    def on_modified(self, event):
        if event.src_path == self.file_path:
            with open(self.file_path, "r") as file:
                file.seek(self.last_position)
                lines = file.readlines()
                self.last_position = file.tell()

                for line in lines:
                    if CONFIG["keyword_from"] in line:
                        content_lines = []
                        content_lines.append(line.strip())

                        # Read subsequent lines until keyword_end is found
                        for subsequent_line in lines[lines.index(line) + 1:]:
                            content_lines.append(subsequent_line.strip())
                            if CONFIG["keyword_end"] in subsequent_line:
                                break

                        content = "\n".join(content_lines)

                        # Check if the content is the same as the last sent log
                        if content != self.last_sent_log:
                            send_telegram_message(CONFIG["title"], content)
                            self.last_sent_log = content

# Inisialisasi dan mulai observer
if __name__ == "__main__":
    event_handler = LogFileHandler(log_file_path)
    observer = Observer()
    observer.schedule(event_handler, path=log_file_path, recursive=False)

    print("Watching for log updates...")
    try:
        observer.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
