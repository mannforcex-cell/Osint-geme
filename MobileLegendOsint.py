import os
import requests
import time

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
 {C}      OSINT MLBB MULTI-TRACKER {W}
 {Y}      Created by: Mann Force (Cyber Force X) {W}
 {R}================================================={W}
    """)

def mlbb_osint():
    print(f"\n{C}[?] Taip 'exit' pada ID kalau nak tubik.{W}")
    uid = input(f"{Y}[+] Masukkan ID MLBB   : {W}")
    
    if uid.lower() == 'exit':
        return False
        
    zone = input(f"{Y}[+] Masukkan Zone ID   : {W}")

    # Gabung ID dan Zone untuk API
    api_url = f"https://api.nexray.eu.cc/stalker/mlbb?id={uid}&zone={zone}"
    
    try:
        print(f"\n{C}[*] Sedang scan database Moonton... rilek jap...{W}")
        time.sleep(1.2) # Fake loading sikit
        
        req = requests.get(api_url, timeout=10)
        data = req.json()
        
        if data.get('status'):
            res = data.get('result', {})
            
            # Ekstrak info dari JSON
            username = res.get('username', 'N/A')
            region = res.get('region', 'N/A')
            acc_id = res.get('id', uid)
            acc_zone = res.get('zone', zone)
            
            clear_screen()
            banner()
            print(f"{G}[+] SUCCESS! Data player berjaya ditarik!{W}\n")
            
            print(f"{C}" + "═"*45 + f"{W}")
            print(f"{R}          ♦ DATA TARGET MOBILE LEGENDS ♦        {W}")
            print(f"{C}" + "═"*45 + f"{W}")
            print(f"{Y}[+] Nickname     :{W} {username}")
            print(f"{Y}[+] ID Target    :{W} {acc_id}")
            print(f"{Y}[+] Zone ID      :{W} {acc_zone}")
            print(f"{Y}[+] Server Region:{W} {region}")
            print(f"{C}" + "═"*45 + f"{W}")
        else:
            print(f"\n{R}[-] Gagal. ID/Zone salah atau akaun tu hidden boh.{W}")
            
    except Exception as e:
        print(f"\n{R}[-] Ralat Server: {e}{W}")
        
    return True

def main():
    clear_screen()
    banner()
    while True:
        if not mlbb_osint():
            print(f"\n{G}[!] Bereh bos, sistem ditutup. Ciao!{W}")
            break

if __name__ == "__main__":
    main()
