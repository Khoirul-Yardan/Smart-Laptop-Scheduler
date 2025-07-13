# 💻 Smart Laptop Scheduler

Sebuah aplikasi ringan berbasis Python dan Streamlit untuk membantu pengguna laptop dengan spesifikasi rendah (RAM kecil, CPU pas-pasan) agar tetap bisa memantau, menganalisis, dan mengontrol aplikasi yang mengonsumsi sumber daya besar secara real-time.

---

## 🚀 Fitur Utama

- 🔁 **Auto-refresh tiap 5 detik** menggunakan `streamlit_autorefresh`
- 🧠 **Analisis CPU & RAM secara real-time**
- 🧹 **Tampilkan proses berat (CPU > 20%)**
- 💣 **Tombol "Kill" untuk menghentikan aplikasi berat**
- 🔐 **Proteksi proses sistem** agar tidak terhentikan sembarangan
- 📊 **Tampilkan aplikasi dengan penggunaan RAM terbesar**
- 🧭 **Rekomendasi otomatis** berdasarkan performa saat ini

---


## 📥 Instalasi

1. Clone / Download Proyek

2. Install Library

pip install -r requirements.txt

Pastikan kamu menggunakan Python versi 3.8 atau lebih baru.

▶️ Cara Menjalankan

streamlit run main.py

Tunggu beberapa detik, lalu aplikasi akan terbuka otomatis di browser.

🧠 Daftar Ketergantungan (dependencies)
- streamlit

- psutil

- pandas

- streamlit_autorefresh

⚠️ Catatan Penting
Aplikasi ini tidak akan menghentikan proses sistem penting seperti System, winlogon.exe, dll.

Jika kamu menjalankan aplikasi dengan akses administrator, beberapa proses bisa lebih terlihat/dikontrol.

Hanya proses yang menggunakan CPU tinggi atau RAM besar yang ditampilkan untuk efisiensi.

🧩 Pengembangan Selanjutnya (Opsional) : 

🔘 Pause/Suspend proses sementara

📊 Grafik performa CPU/RAM dari waktu ke waktu

💾 Logging ke dalam file .csv atau .json

🌐 Web deploy ke server lokal/internet

## 🧑‍💻 Author
Khoirul Yardan
Mahasiswa D3 Teknik Informatika
Dengan bimbingan ide dari OpenAI ChatGPT
GitHub: github.com/khoirul-yardan

