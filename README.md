## Killua-Bot V2 : Next-Gen AI Chatbot

**Killua-Bot V2** adalah aplikasi asisten interaktif berbasis *Command Line Interface* (CLI) yang menggabungkan kecerdasan buatan **Gemini AI Engine** dengan berbagai perkakas utilitas sistem (*system utilities*). 

---

## Fitur

*   **Smart AI Chatbot Interaction:** Terintegrasi langsung dengan API Gemini AI (`gemini-1.5-flash`). Bot memiliki memori kontekstual untuk mengingat alur percakapan secara natural.
*   **Dynamic Authentication Gateway:** Keamanan tingkat lanjut yang meminta ID Pengguna dan API Key langsung di terminal saat *runtime* (mencegah kebocoran API Key di GitHub).
*   **System Diagnostics:** Modul pengecekan arsitektur OS, informasi prosesor, serta spesifikasi mesin secara real-time.
*   **Network Tools:** Fitur pencarian IP Private (lokal), IP Public (via eksternal API), serta utilitas `Ping` jaringan yang disesuaikan untuk dependensi Linux.
*   **Clean Architecture:** Struktur kode terpisah secara modular (`core/`, `config.py`, `main.py`) memudahkan pengembangan lanjut (*scalability*).

---

## 🛠️ Panduan Instalasi

Ikuti langkah-langkah berikut untuk memasang dan menjalankan Killua-Bot V2 di laptop Xubuntu atau distro Linux lainnya:

### 1. Kloning Repository
Buka terminal Xubuntu kamu, lalu unduh proyek ini dari GitHub:
```bash
git clone [https://github.com/username-kamu/killua-v2.git](https://github.com/username-kamu/killua-v2.git)
cd killua-v2
