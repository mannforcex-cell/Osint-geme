import os
import requests
import time
from datetime import datetime

# --- WARNA UNTUK TERMINAL BIAR BERGAYA ---
R = '\033[91m'  # Merah
G = '\033[92m'  # Hijau
Y = '\033[93m'  # Kuning
C = '\033[96m'  # Cyan
W = '\033[0m'   # Putih/Reset

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(f"""{R}
 ▄▄▄██▀▀▀ ██▓ ███▄ ▄███▓ ▄▄▄       ███▄    █ 
   ▒██    ▓██▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
   ░██    ▒██▒▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
▓██▄██▓   ░██░▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
 ▓███▒    ░██░▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒▓▒▒░    ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 {C}      OSINT TIKTOK MULTI-TRACKER {W}
 {Y}      Created by: Mann Force (Cyber Force X) {W}
 {R}================================================={W}
    """)

def tiktok_osint():
    print(f"\n{C}[?] Taip 'exit' pada username kalau nak tubik.{W}")
    username = input(f"{Y}[+] Masukkan Username TikTok (tanpa @) : {W}")
    
    if username.lower() == 'exit':
        return False

    api_url = f"https://api.nexray.eu.cc/stalker/tiktok?username={username}"
    
    try:
        print(f"\n{C}[*] Sedang bypass server ByteDance... rilek jap...{W}")
        time.sleep(1.2) # Fake loading sikit bagi gempak
        
        req = requests.get(api_url, timeout=10)
        data = req.json()
        
        if data.get('status'):
            res = data.get('result', {})
            
            # Ekstrak maklumat basic
            uid = res.get('id', 'N/A')
            user = res.get('username', 'N/A')
            name = res.get('name', 'N/A')
            link = res.get('link', 'N/A')
            verified = res.get('verified', 'Unverified')
            private = res.get('private', 'No')
            region = res.get('region', 'N/A')
            
            # Bersihkan bio dari newline
            bio = res.get('bio', 'Tiada Bio')
            if bio and isinstance(bio, str):
                bio = bio.replace('\n', ' | ').replace('\r', '')
            else:
                bio = 'Tiada Bio'
                
            # Tukar Epoch Time kepada Tarikh yang boleh dibaca
            create_time = res.get('create_time', 0)
            if create_time:
                try:
                    dt_object = datetime.fromtimestamp(create_time)
                    created_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    created_date = "N/A"
            else:
                created_date = "N/A"
                
            # Ekstrak Stats
            stats = res.get('stats', {})
            followers = stats.get('followers', '0')
            following = stats.get('following', '0')
            likes = stats.get('likes', '0')
            videos = stats.get('videos', '0')
            
            clear_screen()
            banner()
            print(f"{G}[+] SUCCESS! Data target berjaya ditarik!{W}\n")
            
            print(f"{C}" + "═"*55 + f"{W}")
            print(f"{R}               ♦ DATA TARGET TIKTOK ♦        {W}")
            print(f"{C}" + "═"*55 + f"{W}")
            print(f"{Y}[+] Nama         :{W} {name}")
            print(f"{Y}[+] Username     :{W} @{user}")
            print(f"{Y}[+] ID TikTok    :{W} {uid}")
            print(f"{Y}[+] Status Acc   :{W} {verified} (Private: {private})")
            print(f"{Y}[+] Region       :{W} {region}")
            print(f"{Y}[+] Bio Target   :{W} {bio}")
            print(f"{Y}[+] Link Profile :{W} {link}")
            print(f"{C}" + "─" * 55 + f"{W}")
            print(f"{Y}[+] Total Video  :{W} {videos}")
            print(f"{Y}[+] Followers    :{W} {followers}")
            print(f"{Y}[+] Following    :{W} {following}")
            print(f"{Y}[+] Total Likes  :{W} {likes}")
            print(f"{C}" + "─" * 55 + f"{W}")
            print(f"{Y}[+] Tarikh Dibuat:{W} {created_date}")
            print(f"{C}" + "═"*55 + f"{W}")
        else:
            print(f"\n{R}[-] Gagal. Username salah atau akaun dah kena ban.{W}")
            
    except Exception as e:
        print(f"\n{R}[-] Ralat Server: {e}{W}")
        
    return True

def main():
    clear_screen()
    banner()
    while True:
        if not tiktok_osint():
            print(f"\n{G}[!] Bereh bos, sistem ditutup. Ciao!{W}")
            break

if __name__ == "__main__":
    main()
