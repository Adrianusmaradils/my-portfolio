import os
import shutil

# Tentukan folder yang ingin dirapikan (misal folder Downloads)
# Gunakan path lengkap, contoh: '/home/username/Downloads'
target_dir = os.path.expanduser("~/Downloads")

# Definisi kategori file dan ekstensinya
folders = {
    "Dokumen": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Video": [".mp4", ".mkv", ".mov", ".avi"],
    "Musik": [".mp3", ".wav", ".flac"],
    "Arsip": [".zip", ".rar", ".tar", ".gz"],
    "Installer": [".deb", ".rpm", ".sh"]
}

def organize_files():
    # Pastikan folder target ada
    if not os.path.exists(target_dir):
        print(f"Folder {target_dir} tidak ditemukan.")
        return

    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)

        # Lewati jika itu adalah folder
        if os.path.isdir(filepath):
            continue

        # Ambil ekstensi file
        file_ext = os.path.splitext(filename)[1].lower()

        # Cari kategori yang cocok
        moved = False
        for folder_name, extensions in folders.items():
            if file_ext in extensions:
                dest_folder = os.path.join(target_dir, folder_name)
                
                # Buat folder kategori jika belum ada
                os.makedirs(dest_folder, exist_ok=True)
                
                # Pindahkan file
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f"✅ Dipindahkan: {filename} -> {folder_name}/")
                moved = True
                break
        
        if not moved:
            print(f"ℹ️ Dilewati (Tanpa Kategori): {filename}")

if __name__ == "__main__":
    print(f"Mulai merapikan: {target_dir}...")
    organize_files()
    print("Selesai!")
