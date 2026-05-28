import google.generativeai as genai
import config

class GeminiEngine:
    def __init__(self):
        # Menginisialisasi API menggunakan Key yang diinput user
        genai.configure(api_key=config.API_KEY)
        
        # Menggunakan model gemini-1.5-flash (cepat dan efisien untuk CLI)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=(
                f"Kamu adalah Killua-Bot V2, asisten AI pintar yang responsif, ramah, dan keren. "
                f"Kamu sedang mengobrol dengan {config.USER_ID}. Jawablah pertanyaannya dengan santai "
                f"namun tetap informatif. Gunakan gaya bahasa anak muda Indonesia yang sopan."
            )
        )
        # Memulai sesi chat agar bot memiliki memori konteks obrolan
        self.chat = self.model.start_chat(history=[])

    def send_message(self, prompt: str) -> str:
        """Mengirim pesan ke Gemini AI dan mengembalikan respons teks"""
        try:
            response = self.chat.send_message(prompt)
            return response.text
        except Exception as e:
            return f"{config.RED}Gagal terhubung ke AI. Error: {str(e)}{config.RESET}"
