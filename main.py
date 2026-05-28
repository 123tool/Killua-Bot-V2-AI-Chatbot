#!/usr/bin/env python3
import sys
import config
from core import tools
from core.ai import GeminiEngine

def main():
    # 1. Jalankan inisialisasi ID dan API Key di awal terminal
    config.initialize_auth()
    
    # 2. Bangun Engine Gemini AI setelah dapet API Key valid
    try:
        ai_bot = GeminiEngine()
    except Exception as e:
        print(f"{config.RED}[!] Gagal membangun AI Engine: {e}{config.RESET}")
        sys.exit(1)
        
    # 3. Bersihkan layar dan cetak banner profesional
    config.print_banner()
    
    # Pesan pembuka awal bot
    print(f"{config.CYAN}Killua-Bot {config.WHITE}: Selamat datang, {config.YELLOW}{config.USER_ID}{config.WHITE}!")
    print(f"{config.CYAN}Killua-Bot {config.WHITE}: Ketik {config.GREEN}menu{config.WHITE} untuk melihat daftar utility tool.")
    print(f"{config.CYAN}Killua-Bot {config.WHITE}: Atau langsung ketik pesan apa saja untuk mengobrol dengan AI.\n")

    # 4. Loop Utama Chatbot (Infinite Loop)
    try:
        while True:
            # Mengambil input dari user di terminal
            user_input = input(f"{config.YELLOW}{config.USER_ID} {config.WHITE}: {config.RESET}").strip()
            
            # Jika user memencet enter tanpa mengetik apa-apa
            if not user_input:
                continue
                
            # Jalankan Logika Routing Perintah Kontrol
            if user_input.lower() == "menu":
                tools.show_menu()
                
            elif user_input == "!Cek IP Private":
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: IP Private Anda adalah {config.YELLOW}{tools.get_private_ip()}\n")
                
            elif user_input == "!Cek IP Public":
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: Menghubungi server ipify...")
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: IP Public Anda adalah {config.YELLOW}{tools.get_public_ip()}\n")
                
            elif user_input == "!Cek Hari":
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: Hari ini adalah hari {config.YELLOW}{tools.get_current_day()}\n")
                
            elif user_input == "!Cek Jam":
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: Waktu sekarang menunjukkan {config.YELLOW}{tools.get_current_time()}\n")
                
            elif user_input == "!Cek System":
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: {tools.get_system_info()}\n")
                
            elif user_input == "!Ping":
                tools.execute_ping()
                print()
                
            elif user_input == "!Short-link":
                tools.create_shortlink()
                print()
                
            elif user_input == "!Cek Pintar":
                gauge = tools.generate_fake_gauge()
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: Menganalisis tingkat kecerdasan...\n{gauge}\n")
                
            elif user_input == "!Cek Engine Name":
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: Nama Engine saya adalah {config.GREEN}Killua-Bots V2 Enterprise AI\n")
                
            elif user_input == "!Cek Project Author":
                print(f"""
  {config.WHITE}┌───[ PROJECT CREDITS ]───┐
  │ Author    : {config.YELLOW}Rolandino (SPY-E)
  │ Base Code : {config.YELLOW}HunxByts Framework (Upgraded)
  │ Machine   : {config.YELLOW}Xubuntu Linux Environment
  └─────────────────────────┘\n""")
                
            elif user_input.lower() in ["exit", "quit", "goodbye"]:
                print(f"{config.RED}Killua-Bot : Mematikan engine... Sampai jumpa, {config.USER_ID}!{config.RESET}")
                break
                
            # 5. Jika bukan perintah '!', lempar obrolan langsung ke Gemini AI
            else:
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: {config.MAGENTA}[AI Thinking...]{config.RESET}\r", end="")
                ai_response = ai_bot.send_message(user_input)
                # Bersihkan baris [AI Thinking...] lalu cetak hasil respon asli
                sys.stdout.write("\033[K") 
                print(f"{config.CYAN}Killua-Bot {config.WHITE}: {ai_response}\n")

    except KeyboardInterrupt:
        print(f"\n\n{config.RED}[!] Menutup paksa program. Bot Berhenti...{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
