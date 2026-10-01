🕷️ AUTO WEB CRAWLER v2.0

Wordlist-Free Reconnaissance & Surface Discovery Engine

 ██████╗██████╗  █████╗ ██╗    ██╗██╗     ███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗██║    ██║██║     ██╔════╝██╔══██╗
██║     ██████╔╝███████║██║ █╗ ██║██║     █████╗  ██████╔╝
██║     ██╔══██╗██╔══██║██║███╗██║██║     ██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║╚███╔███╔╝███████╗███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝╚═╝  ╚═╝
 
[ Automated Link Extraction // Zero-Wordlist Dependency ]


📌 Executive Summary

Auto Web Crawler v2.0 adalah instrumen Passive Reconnaissance cerdas berbasis Python. Berbeda dengan directory fuzzer konvensional, engine ini tidak membutuhkan wordlist. Program akan bertindak sebagai "Spider", menyusup ke halaman utama target, membedah struktur HTML-nya, dan mengekstrak semua direktori serta tautan yang tersembunyi secara otomatis dan instan.

✨ Fitur Utama

🚫 Zero-Wordlist Dependency: Ucapkan selamat tinggal pada file text tebakan yang berat. Crawler murni memetakan apa yang ada di dalam struktur website.

🧠 Smart HTML Parsing: Menggunakan BeautifulSoup4 untuk mengekstrak seluruh tag <a> dan href dengan akurasi tinggi.

🔗 Auto URL Joining: Mampu mengonversi relative path (seperti /admin/login.php) menjadi absolute URL secara otomatis.

🧹 Anti-Duplikasi: Dilengkapi dengan algoritma berbasis Set() untuk memastikan tidak ada link ganda dalam hasil scan kamu.

🛡️ Graceful Error Handling: Tidak akan crash saat menghadapi masalah koneksi atau input URL yang tidak valid.

⚙️ Persyaratan Sistem

Pastikan sistem kamu sudah terinstal Python 3.x. Karena tool ini menggunakan library pihak ketiga untuk pembedahan HTML, kamu wajib menginstal dependencies berikut:

pip install requests beautifulsoup4


🚀 Instalasi & Cara Penggunaan

Clone repositori ini ke sistem lokal kamu:

git clone https://github.com/kenkaiken67/Auto_Web_Crawler.git
cd Auto_Web_Crawler


Eksekusi Engine:
Buka terminal kamu dan jalankan script dengan perintah berikut:

python crawler.py


Input Target:
Saat prompt muncul, masukkan URL target yang ingin dipetakan.

Masukkan URL Target (contoh: http://testphp.vulnweb.com) : http://target-edukasi.com


⚠️ Disclaimer of Liability

Instrumen ini dikembangkan MURNI UNTUK TUJUAN EDUKASI DAN PENELITIAN KEAMANAN ETIKAL.

Pengembang (Author) tidak bertanggung jawab atas segala bentuk penyalahgunaan, kerusakan sistem, atau pelanggaran hukum yang diakibatkan oleh penggunaan tool ini. Selalu pastikan kamu memiliki otoritas penuh atau izin tertulis (seperti program Bug Bounty resmi) sebelum melakukan pemindaian terhadap target manapun.

Dibuat dengan 💻 untuk komunitas Cyber Security Indonesia.
