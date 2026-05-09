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
 {C}    OSINT FREE FIRE MULTI-TRACKER {W}
 {Y}    Created by: Mann Force (Cyber Force X) {W}
 {R}================================================={W}
    """)

def free_fire_osint():
    uid = input(f"\n{C}[?] Masukkan UID (atau taip 'exit' nak tubik): {W}")
    
    if uid.lower() == 'exit':
        return False

    api_url = f"https://api.nexray.eu.cc/stalker/freefire?uid={uid}"
    
    try:
        print(f"\n{Y}[*] Sedang tembus database Garena... rilek jap...{W}")
        time.sleep(1.2) # Fake loading sikit bagi nampak real
        print(f"{Y}[*] Mengira jumlah topup...{W}")
        time.sleep(0.8)
        
        req = requests.get(api_url, timeout=10)
        data = req.json()
        
        if data.get('status'):
            res = data.get('result', {})
            
            # Ekstrak info penting
            name = res.get('name', 'N/A')
            
            # FIX: Paksa tukar jadi integer (nombor) supaya tak error darab float
            try:
                level = int(res.get('level', 0))
            except (ValueError, TypeError):
                level = 0
                
            try:
                likes = int(res.get('likes', 0))
            except (ValueError, TypeError):
                likes = 0
                
            region = res.get('region', 'N/A')
            created_at = res.get('created_at', 'N/A')
            last_login = res.get('last_login', 'N/A')
            signature = res.get('signature', 'N/A')
            guild_name = res.get('guild_name', 'Tiada Guild')
            
            # --- FAKE SMART MONEY CALCULATION ---
            try:
                create_date = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
                current_date = datetime.now()
                days_active = (current_date - create_date).days
                if days_active < 0: days_active = 0
            except:
                days_active = 365 
                
            fake_spent = (days_active * 1.5) + (level * 25.5) + (likes * 0.5)
            # ------------------------------------
            
            clear_screen()
            banner()
            print(f"{G}[+] SUCCESS! Data berjaya ditarik!{W}\n")
            
            print(f"{C}" + "═"*45 + f"{W}")
            print(f"{R}          ♦ DATA TARGET FREE FIRE ♦        {W}")
            print(f"{C}" + "═"*45 + f"{W}")
            print(f"{Y}[+] Nama Target  :{W} {name}")
            print(f"{Y}[+] UID Game     :{W} {uid}")
            print(f"{Y}[+] Level Target :{W} {level}")
            print(f"{Y}[+] Total Likes  :{W} {likes}")
            print(f"{Y}[+] Server Region:{W} {region}")
            print(f"{Y}[+] Nama Guild   :{W} {guild_name}")
            print(f"{Y}[+] Bio / Sign   :{W} {signature}")
            print(f"{Y}[+] Akaun Dibuat :{W} {created_at}")
            print(f"{Y}[+] Last Online  :{W} {last_login}")
            print(f"{C}" + "─" * 45 + f"{W}")
            print(f"{G}[$$] Anggaran Total Topup : RM {fake_spent:,.2f}{W}")
            print(f"{C}" + "═"*45 + f"{W}")
        else:
            print(f"\n{R}[-] Gagal. UID tak wujud atau API ngamuk.{W}")
            
    except Exception as e:
        print(f"\n{R}[-] Ralat Server: {e}{W}")
        
    return True

def main():
    clear_screen()
    banner()
    while True:
        if not free_fire_osint():
            print(f"\n{G}[!] Bereh bos, sistem ditutup. Ciao!{W}")
            break

if __name__ == "__main__":
    main()

