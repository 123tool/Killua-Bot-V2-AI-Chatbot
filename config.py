import os
import sys

# --- KONFIGURASI WARNA ANSI (Rich Terminal Experience) ---
RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'

# --- MANAJEMEN API & AUTHENTICATION ---
API_KEY = None
USER_ID = "User"

def initialize_auth():
    """Fungsi untuk meminta ID dan API Key Gemini AI di awal program"""
    global API_KEY, USER_ID
    os.system('clear')
    
    print(f"{CYAN}{BOLD}┌───[ ENTERPRISE BOT INITIALIZATION ]───┐{RESET}")
    
    # Input User ID
    user_input = input(f"{WHITE}│ Masukkan ID / Nama Anda : {YELLOW}").strip()
    if user_input:
        USER_ID = user_input
        
    # Input API Key
    print(f"{WHITE}│ Dapatkan API Key di: https://aistudio.google.com/")
    api_input = input(f"{WHITE}│ Masukkan Gemini API Key : {YELLOW}").strip()
    
    if not api_input:
        print(f"{RED}│ Error: API Key tidak boleh kosong! Program keluar.{RESET}")
        sys.exit(1)
        
    API_KEY = api_input
    print(f"{CYAN}└───[ AUTENTIKASI BERHASIL ]───┘{RESET}\n")
    print(f"{GREEN}[*] Mengonfigurasi engine AI... Mohon tunggu.{RESET}")

def print_banner():
    """Mencetak identitas bot yang sudah didesain ulang agar tidak terkesan duplikat"""
    os.system('clear')
    banner = f"""{CYAN}
 ▄▄▄▄    ▒█████  ▄▄▄█████▓ ▄▄▄█████▓ ▓█████  ██▀███  
▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒ ▓  ██▒ ▓▒ ▓█   ▀ ▓██ ▒ ██▒
▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒─ ▒ ▓██░ ▒─ ▒███   ▓██ ░▄█ ▒
▒██░█▀  ▒██   ██░░ ▓██▓ ░  ░ ▓██▓ ░  ▒▓█  ▄ ▒██▀▀█▄  
░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░    ▒██▒ ░  ░▒████▒░██▓ ▒██▒
 ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░      ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒░▒   ░   ░ ▒ ▒░     ░         ░     ░ ░  ░  ░▒ ░ ▒░
  ░    ░ ░ ░ ░ ▒    ░         ░         ░     ░░   ░ 
  ░          ░ ░                        ░  ░   ░     
       ░                                             
{WHITE}  [ NEXT-GEN AI CHATBOT & UTILITIES ENGINE ]
  {CYAN}Fork & Re-Coded By: {WHITE}Rolandino (SPY-E) | Version 2.0
{WHITE}<<=============================================================>>{RESET}"""
    print(banner)
