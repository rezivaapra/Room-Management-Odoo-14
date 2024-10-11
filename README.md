# Panduan Instalasi Odoo 14 dan Custom Addons di Windows

## Deskripsi

Dokumen ini menyediakan langkah-langkah untuk menginstal Odoo 14 serta menginstal custom addons di sistem operasi Windows.

## Prasyarat

Sebelum memulai instalasi, pastikan Anda memiliki:

- Sistem operasi: Windows 10 atau lebih baru
- Python 3.6 atau lebih baru
- PostgreSQL 10 atau lebih baru
- Git
- Visual Studio Build Tools (untuk mengkompilasi dependensi)

## Instalasi Odoo 14

### 1. Menginstal Dependensi

1. **Instal Python**: Unduh dan instal Python dari [python.org](https://www.python.org/downloads/). Pastikan untuk mencentang opsi "Add Python to PATH" saat instalasi.

2. **Instal PostgreSQL**: Unduh dan instal PostgreSQL dari [postgresql.org](https://www.postgresql.org/download/windows/). Saat instalasi, buat user PostgreSQL baru bernama `odoo14` dengan password `admin`.

3. **Instal Git**: Unduh dan instal Git dari [git-scm.com](https://git-scm.com/download/win).

4. **Instal Visual Studio Build Tools**: Unduh dan instal dari [Visual Studio](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

### 2. Mengunduh Odoo 14

1. Buka Command Prompt dan jalankan perintah berikut untuk mengunduh Odoo 14:

   ```bash
   git clone https://www.github.com/odoo/odoo --depth 1 --branch 14.0 --single-branch

## Menginstal Paket Python

1. Masuk ke direktori Odoo yang telah diunduh:
    ```
    cd odoo
2. Instal paket Python yang diperlukan:
    ```
    pip install -r requirements.txt
## Mengonfigurasi Odoo
1. Buat file konfigurasi Odoo. Anda bisa menggunakan Notepad untuk membuat file baru bernama odoo.conf:
    ```
    [options]
    ; This is the password that allows database operations:
    admin_passwd = admin
    db_host = False
    db_port = False
    db_user = odoo14
    db_password = admin
    addons_path = C:\path\to\your\addons
    logfile = C:\path\to\your\odoo.log
Ganti C:\path\to\your\addons dengan jalur ke direktori addons Anda.
## Menjalankan Odoo
Jalankan Odoo dengan perintah berikut di Command Prompt:
   ```
   python odoo-bin -c config.conf
   ```
Akses Odoo melalui browser di http://localhost:port
