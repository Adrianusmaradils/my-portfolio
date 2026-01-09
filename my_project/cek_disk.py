import shutil
import os

def check_disk_usage():
    # Mengambil data penggunaan disk pada root (/)
    total, used, free = shutil.disk_usage("/")

    # Konversi ke Gigabyte (GB)
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)
    
    # Hitung persentase penggunaan
    percent_used = (used / total) * 100

    print("-" * 30)
    print(f"Laporan Penyimpanan Sistem")
    print("-" * 30)
    print(f"Total Kapasitas: {total_gb} GB")
    print(f"Digunakan       : {used_gb} GB ({percent_used:.2f}%)")
    print(f"Tersedia        : {free_gb} GB")
    print("-" * 30)

    # Memberikan peringatan jika penggunaan di atas 80%
    if percent_used > 80:
        print("⚠️ PERINGATAN: Ruang penyimpanan Anda hampir penuh!")
    else:
        print("✅ Status: Ruang penyimpanan masih aman.")

if __name__ == "__main__":
    check_disk_usage()
