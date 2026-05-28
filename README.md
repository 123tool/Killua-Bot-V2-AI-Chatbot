## Killua Bot V2 AI Chatbot

---

**Killua Bot V2** adalah aplikasi asisten interaktif berbasis *Command Line Interface* (CLI) yang menggabungkan kecerdasan buatan **Gemini AI Engine** dengan berbagai perkakas utilitas sistem (*system utilities*). 

---

## Fitur

*   **Smart AI Chatbot Interaction :** Terintegrasi langsung dengan API Gemini AI (`gemini-1.5-flash`). Bot memiliki memori kontekstual untuk mengingat alur percakapan secara natural.
*   **Dynamic Authentication Gateway :** Keamanan tingkat lanjut yang meminta ID Pengguna dan API Key langsung di terminal saat *runtime* (mencegah kebocoran API Key di GitHub).
*   **System Diagnostics :** Modul pengecekan arsitektur OS, informasi prosesor, serta spesifikasi mesin secara real-time.
*   **Network Tools :** Fitur pencarian IP Private (lokal), IP Public (via eksternal API), serta utilitas `Ping` jaringan yang disesuaikan untuk dependensi Linux.
*   **Clean Architecture :** Struktur kode terpisah secara modular (`core/`, `config.py`, `main.py`) memudahkan pengembangan lanjut (*scalability*).

---

## 🛠️ Panduan Instalasi

Ikuti langkah-langkah berikut untuk memasang dan menjalankan Killua-Bot V2 di laptop Xubuntu atau distro Linux lainnya :

1. Kloning Repository
Buka terminal Xubuntu kamu, lalu unduh proyek ini dari GitHub :
```bash
git clone https://github.com/123tool/Killua-Bot-V2-AI-Chatbot.git
cd Killua-Bot-V2-AI-Chatbot
```
2. Install Dependensi Modul
​Pastikan Python 3 dan PIP sudah terinstal. Jalankan perintah ini untuk memasang SDK Google GenAI resmi beserta library pendukungnya :
```
pip install google-generativeai requests
```
3. Atur Hak Akses Eksekusi
​Agar skrip utama dapat dieksekusi langsung sebagai binary tool tanpa harus mengetik python3 :
```
chmod +x main.py
```

---

## Cara Penggunaan

1. ​Jalankan program melalui terminal dengan perintah :
```
   ./main.py
```
2. ​Proses Autentikasi : Bot akan meminta Anda memasukkan nama/ID beserta Gemini API Key.
​Catatan : Jika belum memiliki API Key, Anda bisa mendapatkannya secara gratis melalui Google AI Studio.
3. ​Setelah masuk ke halaman utama, ketik menu untuk memunculkan daftar perintah utilitas kontrol.

---

## Perintah Utilitas Tersedia (`!`)

| Perintah | Fungsi |
| :--- | :--- |
| `menu` | Menampilkan seluruh daftar menu bantuan |
| `!Cek IP Private` | Memeriksa IP Address lokal komputer Anda |
| `!Cek IP Public` | Memeriksa IP Publik internet yang sedang digunakan |
| `!Cek Hari` | Menampilkan hari saat ini (Bahasa Indonesia) |
| `!Cek Jam` | Menampilkan waktu lokal aktual |
| `!Cek System` | Menampilkan informasi OS, Kernel, dan Prosesor Xubuntu |
| `!Ping` | Melakukan tes koneksi ICMP ke URL/IP Target |
| `!Short-link` | Memendekkan URL panjang menggunakan API TinyURL |
| `!Cek Pintar` | Fitur hiburan kalkulator persentase kecerdasan acak |
| `!Cek Engine Name` | Menampilkan identitas versi engine bot yang aktif |
| `!Cek Project Author` | Menampilkan kredibilitas pengembang proyek |

---

## Kelebihan

Jika Anda mengetik apa pun selain perintah berawalan tanda seru (`!`) di atas, pesan Anda akan langsung diproses secara cerdas oleh Gemini AI sebagai obrolan biasa.

---

## Kontribusi

​Kontribusi, pelaporan bug, maupun saran penambahan fitur selalu terbuka lebar. Silakan lakukan Fork repository ini dan buat Pull Request, atau buka bagian Issues.
