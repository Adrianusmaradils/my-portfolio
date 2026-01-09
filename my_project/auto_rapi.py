import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Tentukan folder yang diawasi
target_dir = os.path.expanduser("~/Downloads")

# Definisi kategori file
folders = {
    "Dokumen": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
    "Musik": [".mp3", ".wav", ".flac"],
    "Arsip": [".zip", ".rar", ".tar", ".gz"],
    "Installer": [".deb", ".rpm", ".sh"]
}

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Saat folder berubah, jalankan fungsi perapian
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            
            if os.path.isdir(filepath):
                continue

            file_ext = os.path.splitext(filename)[1].lower()
            
            for folder_name, extensions in folders.items():
                if file_ext in extensions:
                    dest_folder = os.path.join(target_dir, folder_name)
                    os.makedirs(dest_folder, exist_ok=True)
                    
                    # Beri sedikit jeda agar file selesai di-download sepenuhnya
                    time.sleep(1) 
                    
                    try:
                        shutil.move(filepath, os.path.join(dest_folder, filename))
                        print(f"Otomatis memindah: {filename}")
                    except Exception as e:
                        print(f"Gagal memindah {filename}: {e}")

if __name__ == "__main__":
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, target_dir, recursive=False)
    
    print(f"Monitor aktif di: {target_dir}")
    print("Tekan Ctrl+C untuk berhenti.")
    observer.start()
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
