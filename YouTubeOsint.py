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
 {C}      OSINT YOUTUBE MULTI-TRACKER {W}
 {Y}      Created by: Mann Force (Cyber Force X) {W}
 {R}================================================={W}
    """)

def youtube_osint():
    print(f"\n{C}[?] Taip 'exit' pada username kalau nak tubik.{W}")
    username = input(f"{Y}[+] Masukkan Username YouTube (cth: @manforcex) : {W}")
    
    if username.lower() == 'exit':
        return False

    # Buang '@' kalau user ter-type, sebab ada setengah API sensitif
    # Tapi kalau API perlukan '@', boleh buang baris .replace ni.
    clean_username = username.replace('@', '')
    
    api_url = f"https://api.nexray.eu.cc/stalker/youtube?username={clean_username}"
    
    try:
        print(f"\n{C}[*] Sedang ceroboh pelayan Google... rilek jap...{W}")
        time.sleep(1.2) # Fake loading sikit bagi gempak
        
        req = requests.get(api_url, timeout=10)
        data = req.json()
        
        if data.get('status'):
            res = data.get('result', {})
            channel = res.get('channel', {})
            
            # Ekstrak maklumat basic
            user = channel.get('username', 'N/A')
            
            # Handle kalau name tu null/None
            name = channel.get('name')
            if not name:
                name = "Tiada Nama"
                
            subs = channel.get('subscriberCount', '0')
            videos = channel.get('videoCount', '0')
            url = channel.get('channelUrl', 'N/A')
            
            # Bersihkan description dari newline
            desc = channel.get('description')
            if desc and isinstance(desc, str):
                desc = desc.replace('\n', ' | ').replace('\r', '')
            else:
                desc = 'Tiada Description'
            
            clear_screen()
            banner()
            print(f"{G}[+] SUCCESS! Data target berjaya ditarik!{W}\n")
            
            print(f"{C}" + "═"*55 + f"{W}")
            print(f"{R}               ♦ DATA TARGET YOUTUBE ♦        {W}")
            print(f"{C}" + "═"*55 + f"{W}")
            print(f"{Y}[+] Nama Channel :{W} {name}")
            print(f"{Y}[+] Username     :{W} {user}")
            print(f"{Y}[+] Subscribers  :{W} {subs}")
            print(f"{Y}[+] Total Video  :{W} {videos}")
            print(f"{Y}[+] Bio / Desc   :{W} {desc}")
            print(f"{Y}[+] Link Channel :{W} {url}")
            print(f"{C}" + "═"*55 + f"{W}")
        else:
            print(f"\n{R}[-] Gagal. Channel tak wujud atau API sangkut.{W}")
            
    except Exception as e:
        print(f"\n{R}[-] Ralat Server: {e}{W}")
        
    return True

def main():
    clear_screen()
    banner()
    while True:
        if not youtube_osint():
            print(f"\n{G}[!] Bereh bos, sistem ditutup. Ciao!{W}")
            break

if __name__ == "__main__":
    main()
