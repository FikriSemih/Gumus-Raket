#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gümüş Raket Tenis Kulübü & Deuce Cafe — Yerel Sunucu Motoru
Bademli / Bursa
"""

import http.server
import socketserver
import json
import os
import socket
import datetime
import urllib.parse
import webbrowser
import threading

import glob
import re

PORT = 3000
DB_FILE = "gumus_raket_veritabani.json"
BACKUP_DIR = "Yedekler"

def get_latest_html():
    candidates = glob.glob("gumus_raket_v*.html")
    if candidates:
        def version_key(fn):
            nums = re.findall(r'\d+', fn)
            return int(nums[-1]) if nums else 0
        candidates.sort(key=version_key, reverse=True)
        return candidates[0]
    for alt in ["index.html", "gumus_raket_v3.html", "gumus_raket_v2.html"]:
        if os.path.exists(alt):
            return alt
    return "index.html"


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class ClubHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path in ["/", "/index.html", "/app"]:
            target_html = get_latest_html()
            if os.path.exists(target_html):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                with open(target_html, "rb") as f:
                    self.wfile.write(f.read())
                return
            else:
                self.send_error(404, "HTML dosyasi bulunamadi")
                return

        elif path == "/api/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            if os.path.exists(DB_FILE):
                with open(DB_FILE, "rb") as f:
                    self.wfile.write(f.read())
            else:
                self.wfile.write(json.dumps({}).encode("utf-8"))
            return

        elif path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            status_data = {
                "server": "online",
                "club": "Gümüş Raket Tenis Kulübü & Deuce Cafe",
                "location": "Bademli / Bursa",
                "local_ip": get_local_ip(),
                "port": PORT,
                "db_file": DB_FILE,
                "db_exists": os.path.exists(DB_FILE),
                "timestamp": datetime.datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(status_data, ensure_ascii=False, indent=2).encode("utf-8"))
            return

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/sync":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)

            try:
                data = json.loads(body.decode("utf-8"))
                
                # Atomik veritabanı yazımı
                temp_file = DB_FILE + ".tmp"
                with open(temp_file, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                if os.path.exists(DB_FILE):
                    os.replace(temp_file, DB_FILE)
                else:
                    os.rename(temp_file, DB_FILE)

                # Günlük otomatik yedek
                if not os.path.exists(BACKUP_DIR):
                    os.makedirs(BACKUP_DIR)
                
                today_str = datetime.date.today().strftime("%Y-%m-%d")
                backup_file = os.path.join(BACKUP_DIR, f"yedek_{today_str}.json")
                if not os.path.exists(backup_file):
                    with open(backup_file, "w", encoding="utf-8") as bf:
                        json.dump(data, bf, ensure_ascii=False, indent=2)

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "message": "Ana PC veritabanina basariyla kaydedildi", "time": datetime.datetime.now().isoformat()}, ensure_ascii=False).encode("utf-8"))
                return
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "error": str(e)}).encode("utf-8"))
                return

        return super().do_POST()

def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    local_ip = get_local_ip()
    print("=" * 64)
    print("  🎾 GÜMÜŞ RAKET TENİS KULÜBÜ & DEUCE CAFE — YEREL SUNUCU")
    print("  Bademli / Bursa")
    print("=" * 64)
    print(f"  • Ana Bilgisayar (Bu Laptop):   http://localhost:{PORT}")
    print(f"  • Kulüp İçi Wi-Fi Bağlantısı:  http://{local_ip}:{PORT}")
    print(f"  • Veritabanı Dosyası (SSD):     {DB_FILE}")
    print(f"  • Günlük Yedekler Klasörü:     {BACKUP_DIR}/")
    print("=" * 64)
    print("  Sunucu aktif olarak çalışıyor. Bu siyah pencere açık kalmalıdır.")
    print("  Durdurmak için klavyeden CTRL + C tuşlarına basabilirsiniz.")
    print("=" * 64)

    threading.Timer(1.0, open_browser).start()

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), ClubHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nSunucu kapatıldı.")
