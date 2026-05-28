import os
import socket
import requests
import platform
import subprocess
import datetime
import random
import config

def get_private_ip() -> str:
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except Exception:
        return "Tidak dapat mendeteksi IP Lokal"

def get_public_ip() -> str:
    try:
        response = requests.get('https://api.ipify.org/', timeout=5)
        return response.text.strip()
    except requests.RequestException:
        return "Koneksi Offline / Timeout"

def get_current_day() -> str:
    days_map = {
        'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu',
        'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu', 'Sunday': 'Minggu'
    }
    english_day = datetime.datetime.now().strftime('%A')
    return days_map.get(english_day, english_day)

def get_current_time() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')

def get_system_info() -> str:
    info = platform.uname()
    return f"""
  {config.YELLOW}.:: System Diagnostics ::.{config.WHITE}
  OS System : {info.system}
  Node Name : {info.node}
  Release   : {info.release}
  Version   : {info.version}
  Machine   : {info.machine}
  Processor : {info.processor}"""

def generate_fake_gauge() -> str:
    """Memperbaiki fungsi kalkulator acak agar terpakai secara dinamis"""
    gauges = [
        f"{config.WHITE}0%   {config.CYAN}▒▒▒▒▒▒▒▒▒▒",
        f"{config.WHITE}30%  {config.CYAN}███▒▒▒▒▒▒▒",
        f"{config.WHITE}50%  {config.CYAN}█████▒▒▒▒▒",
        f"{config.WHITE}85%  {config.CYAN}████████▒▒",
        f"{config.WHITE}100% {config.CYAN}██████████"
    ]
    return random.choice(gauges)

def execute_ping() -> None:
    host = input(f"\n{config.WHITE}[?] Masukkan URL / IP Target : {config.YELLOW}").strip()
    if not host:
        print(f"{config.RED}[!] Target kosong.")
        return
    try:
        # Menghapus skema http/https jika diinput user
        host_clean = host.replace("https://", "").replace("http://", "").split('/')[0]
        ip_address = socket.gethostbyname(host_clean)
        print(f"{config.GREEN}[*] Ping ke {host_clean} [{ip_address}]...")
        
        # Menyesuaikan parameter ping untuk Linux (Xubuntu menggunakan -c)
        result = subprocess.run(["ping", "-c", "3", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode())
    except socket.gaierror:
        print(f"{config.RED}[!] Domain/URL '{host}' tidak valid atau tidak terjangkau.")

def create_shortlink() -> None:
    """Memperbaiki bug parameter url pada versi terdahulu"""
    url = input(f"\n{config.WHITE}[?] Masukkan URL yang ingin dipendekkan: {config.CYAN}").strip()
    if not url:
        print(f"{config.RED}[!] URL tidak boleh kosong.")
        return
    try:
        response = requests.post(f'http://tinyurl.com/api-create.php?url={url}', timeout=7)
        if response.status_code == 200:
            print(f"{config.GREEN}[+] Hasil URL Singkat : {config.YELLOW}{response.text.strip()}")
        else:
            print(f"{config.RED}[!] Gagal membuat shortlink. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{config.RED}[!] Terjadi kendala jaringan: {e}")

def show_menu():
    print(f"""
          {config.CYAN}.:: {config.WHITE}MENU CONTROL UTILITIES {config.CYAN}::.

  {config.WHITE}[{config.CYAN}1{config.WHITE}] !Cek IP Private          {config.WHITE}[{config.CYAN}6{config.WHITE}]  !Cek System
  {config.WHITE}[{config.CYAN}2{config.WHITE}] !Cek IP Public           {config.WHITE}[{config.CYAN}7{config.WHITE}]  !Ping
  {config.WHITE}[{config.CYAN}3{config.WHITE}] !Cek Hari                {config.WHITE}[{config.CYAN}8{config.WHITE}]  !Short-link
  {config.WHITE}[{config.CYAN}4{config.WHITE}] !Cek Jam                 {config.WHITE}[{config.CYAN}9{config.WHITE}]  !Cek Pintar
  {config.WHITE}[{config.CYAN}5{config.WHITE}] !Cek Project Author      {config.WHITE}[{config.CYAN}10{config.WHITE}] !Cek Engine Name
  
  {config.YELLOW}*Ketik apapun selain perintah di atas untuk mengobrol langsung dengan AI!{config.RESET}
""")
