import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def mulai_crawler(url_target):
    print(f"\n[*] Memulai pemetaan otomatis di : {url_target}")
    
    try:
        # 1. Mengambil halaman web target
        respons = requests.get(url_target)
        
        # 2. Mengecek apakah halaman berhasil diakses (Status 200)
        if respons.status_code == 200:
            print("[+] Halaman berhasil diakses. Sedang mengekstrak struktur web...\n")
            
            # 3. Menganalisis (Parsing) HTML menggunakan BeautifulSoup
            soup = BeautifulSoup(respons.text, 'html.parser')
            
            # 4. Membuat 'set' untuk menampung link agar tidak ada hasil duplikat (ganda)
            kumpulan_link = set() 
            
            # Mencari semua tag <a> yang memiliki atribut 'href' (tempat link berada)
            for tag_a in soup.find_all('a', href=True):
                link_mentah = tag_a['href']
                
                # Menggabungkan link relatif (misal: /login.php) dengan URL utama
                # agar menjadi link utuh (http://target.com/login.php)
                link_lengkap = urljoin(url_target, link_mentah)
                kumpulan_link.add(link_lengkap)
            
            # 5. Menampilkan hasil tangkapan Crawler
            if kumpulan_link:
                print("========================================")
                print(f"      DITEMUKAN {len(kumpulan_link)} TAUTAN/DIREKTORI    ")
                print("========================================")
                for l in kumpulan_link:
                    print(f" -> {l}")
            else:
                print("[-] Tidak ada tautan yang ditemukan di halaman utama ini.")
                
        else:
            print(f"[!] Gagal mengakses halaman. Status Code: {respons.status_code}")
            
    except requests.ConnectionError:
        print(f"\n[!] ERROR: Gagal menyambung ke {url_target}")
        print("Pastikan penulisan URL benar (contoh: http://website.com) dan internet aktif.")
    except Exception as e:
        print(f"\n[!] ERROR Tidak Terduga: {e}")

# === Bagian Utama ===
if __name__ == "__main__":
    print("========================================")
    print("        AUTO WEB CRAWLER (SPIDER)       ")
    print("========================================")
    
    # Meminta input URL dari user secara langsung di terminal
    url_input = input("Masukkan URL Target (contoh: http://testphp.vulnweb.com) : ")
    
    # Memastikan user tidak memasukkan input kosong
    if url_input.strip():
        mulai_crawler(url_input)
    else:
        print("[!] URL tidak boleh kosong!")