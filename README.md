# Linux Smart File Organizer 📂

A Python-based automated file management system that monitors your directories and organizes files into categorized folders based on their extensions. This tool runs as a background system service (Systemd) on Linux.

## 🌟 Features
- **Real-time Monitoring**: Uses the `watchdog` library to detect new files instantly.
- **Auto-Categorization**: Automatically sorts files into folders like `Documents`, `Images`, `Videos`, etc.
- **Background Service**: Runs persistently using Systemd, so it starts automatically on boot.
- **Activity Logging**: Keeps a history of all moved files in `aktivitas_rapi.log`.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Libraries**: `watchdog`, `shutil`, `os`, `logging`
- **System**: Systemd (Linux Service Manager)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone [https://github.com/username_anda/linux-file-organizer.git](https://github.com/username_anda/linux-file-organizer.git)
cd linux-file-organizer