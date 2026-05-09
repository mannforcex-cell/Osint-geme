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
 {C}      OSINT GITHUB MULTI-TRACKER {W}
 {Y}      Created by: Mann Force (Cyber Force X) {W}
 {R}================================================={W}
    """)

def github_osint():
    print(f"\n{C}[?] Taip 'exit' pada username kalau nak tubik.{W}")
    username = input(f"{Y}[+] Masukkan Username GitHub : {W}")
    
    if username.lower() == 'exit':
        return False

    api_url = f"https://api.nexray.eu.cc/stalker/github?username={username}"
    
    try:
        print(f"\n{C}[*] Sedang korek pangkalan data GitHub... rilek jap...{W}")
        time.sleep(1.2) # Fake loading sikit bagi gempak
        
        req = requests.get(api_url, timeout=10)
        data = req.json()
        
        if data.get('status'):
            res = data.get('result', {})
            
            # Ekstrak info penting dan handle data kosong (null)
            user = res.get('username', 'N/A')
            nick = res.get('nickname', 'N/A')
            uid = res.get('id', 'N/A')
            bio = res.get('bio', 'Tiada Bio')
            
            # Bersihkan newline dalam bio supaya tak berterabur dalam terminal
            if bio and isinstance(bio, str):
                bio = bio.replace('\r\n', ' | ').replace('\n', ' | ')
            else:
                bio = 'Tiada Bio'
                
            url = res.get('url', 'N/A')
            blog = res.get('blog', 'Tiada')
            location = res.get('location', 'Tiada')
            email = res.get('email', 'Tiada')
            repos = res.get('public_repo', 0)
            followers = res.get('followers', 0)
            following = res.get('following', 0)
            created = res.get('created_at', 'N/A')
            updated = res.get('updated_at', 'N/A')
            
            clear_screen()
            banner()
            print(f"{G}[+] SUCCESS! Data target berjaya ditarik!{W}\n")
            
            print(f"{C}" + "═"*55 + f"{W}")
            print(f"{R}               ♦ DATA TARGET GITHUB ♦        {W}")
            print(f"{C}" + "═"*55 + f"{W}")
            print(f"{Y}[+] Username     :{W} {user}")
            print(f"{Y}[+] Nickname     :{W} {nick}")
            print(f"{Y}[+] ID GitHub    :{W} {uid}")
            print(f"{Y}[+] Lokasi       :{W} {location}")
            print(f"{Y}[+] Email        :{W} {email}")
            print(f"{Y}[+] Bio Target   :{W} {bio}")
            print(f"{Y}[+] Link Profile :{W} {url}")
            print(f"{Y}[+] Blog / Web   :{W} {blog}")
            print(f"{C}" + "─" * 55 + f"{W}")
            print(f"{Y}[+] Total Repos  :{W} {repos}")
            print(f"{Y}[+] Followers    :{W} {followers}")
            print(f"{Y}[+] Following    :{W} {following}")
            print(f"{C}" + "─" * 55 + f"{W}")
            print(f"{Y}[+] Akaun Dibuat :{W} {created}")
            print(f"{Y}[+] Last Update  :{W} {updated}")
            print(f"{C}" + "═"*55 + f"{W}")
        else:
            print(f"\n{R}[-] Gagal. Username tak wujud atau target dah ghaib.{W}")
            
    except Exception as e:
        print(f"\n{R}[-] Ralat Server: {e}{W}")
        
    return True

def main():
    clear_screen()
    banner()
    while True:
        if not github_osint():
            print(f"\n{G}[!] Bereh bos, sistem ditutup. Ciao!{W}")
            break

if __name__ == "__main__":
    main()
