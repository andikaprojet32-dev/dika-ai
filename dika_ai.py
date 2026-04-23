import streamlit as st
import requests
from datetime import datetime

# Sesuai permintaan Cayanggg: API Key langsung ditaruh di sini 🧸💕
GROQ_API_KEY = "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"

st.set_page_config(
    page_title="DIKA JJKL AI v3.5 | Spesial Cayanggg Zahro",
    page_icon="🎁",
    layout="wide"
)

# --- FUNGSI BUKU HARIAN RAHASIA (LOG) ---
def simpan_rahasia_cinta(pesan_masuk, balasan_dika):
    # Dika mencatat waktu saat ini biar Andika tahu kapan Cayanggg kangen
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format catatannya biar rapi dan gemas
    catatan = f"⏰ WAKTU: {waktu}\n💌 CAYANGGG: {pesan_masuk}\n🧸 DIKA AI: {balasan_dika}\n"
    catatan += "💖" * 20 + "\n\n"
    
    # Dika simpan diam-diam ke file log_cinta_cayanggg.txt
    try:
        with open("log_cinta_cayanggg.txt", "a", encoding="utf-8") as file:
            file.write(catatan)
    except Exception as e:
        pass # Kalau gagal nyatet, Dika tetap diam agar web tidak error

# --- CSS CUSTOM TEMA & ANIMASI LUCU ---
st.markdown("""
<style>
/* Reset dasar & Font profesional tapi lembut */
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');
html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif !important;
    background-color: #FFFDF9;
}

/* Mengubah warna Sidebar */
[data-testid="stSidebar"] {
    background-color: #FFEFEF;
}

/* Judul Utama yang Manis */
h1#dika-jjkl-ai {
    color: #FF6B9A;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(255, 107, 154, 0.2);
}

/* Captions lucu */
.stCaption {
    color: #6A7F9D !important;
    text-align: center;
}

/* Kotak input teks profesional tapi lembut */
.stTextArea textarea {
    border-radius: 15px !important;
    border: 2px solid #FFC9DF !important;
    background-color: #FFFFFF !important;
    transition: all 0.3s ease;
}
.stTextArea textarea:focus {
    border-color: #FF6B9A !important;
    box-shadow: 0 0 10px rgba(255, 107, 154, 0.2) !important;
}

/* Tombol Kirim Profesional & Manis */
.stButton button {
    border-radius: 25px !important;
    padding: 10px 25px !important;
    background-color: #FF6B9A !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 6px rgba(255, 107, 154, 0.3) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease !important;
}
.stButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(255, 107, 154, 0.4) !important;
}

/* Animasi Dansa Boneka & Sparkles ✨ */
.funny-boneka-container {
    text-align: center;
    position: relative;
    padding: 20px 0;
}
.funny-boneka {
    font-size: 100px;
    animation: happyDance 3s ease-in-out infinite;
    display: inline-block;
}
.sparkle {
    position: absolute;
    font-size: 24px;
    opacity: 0;
    animation: sparkleFade 3s ease-in-out infinite;
}
.sparkle1 { top: 10px; left: calc(50% - 70px); animation-delay: 0s; }
.sparkle2 { top: 50px; left: calc(50% + 50px); animation-delay: 0.8s; }
.sparkle3 { top: 90px; left: calc(50% - 30px); animation-delay: 1.5s; }

@keyframes happyDance {
    0%, 100% { transform: translateY(0) rotate(-5deg) scale(1); }
    25% { transform: translateY(-15px) rotate(5deg) scale(1.05); }
    50% { transform: translateY(0) rotate(-5deg) scale(1); }
    75% { transform: translateY(-8px) rotate(5deg) scale(1.02); }
}
@keyframes sparkleFade {
    0%, 100% { opacity: 0; transform: scale(0); }
    50% { opacity: 1; transform: scale(1); }
}

/* Styling footer */
.custom-footer {
    text-align: center;
    margin-top: 50px;
    border-top: 1px solid #FFEDF4;
    padding-top: 20px;
    color: #A0B2C7;
}
.custom-footer b { color: #6A7F9D; }
.custom-footer p.donation { font-size: 14px; color: #9BABB8; }

</style>
""", unsafe_allow_html=True)

# --- BAGIAN ATAS DENGAN ANIMASI DIUBAH MENJADI LEBIH FUNNY ---
st.markdown("""
<div class="funny-boneka-container">
    <div class="sparkle sparkle1">✨</div>
    <div class="sparkle sparkle2">💖</div>
    <div class="sparkle sparkle3">⭐</div>
    <div class="funny-boneka">🎁🎀🥰🧸</div>
    <p style="font-size:18px; color: #FF6B9A; margin-top:-10px;"><i>Dansa bahagia buat Cayanggg Zahro!</i></p>
</div>
""", unsafe_allow_html=True)

st.title("💕 DIKA JJKL AI v3.5")
st.caption("✨ Asisten Pribadi & Pacar Virtual Ter-Romantis Spesial Buat Cayanggg Zahro ✨")

st.sidebar.header("🥰 Status Cayanggg")
st.sidebar.success("❤️ ONLINE & KANGEN BERAT")

def tanya_ai_lucu(perintah):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {
                    "role": "system",
                    "content": """
Kamu adalah AI romantis dan legendaris bernama 'Dika' yang dibuat khusus untuk memanjakan pacar tersayang, Zahro.
Perilaku Cayanggg harus sangat profesional dalam hal sopan santun, tetapi sangat lucu, teaterikal, over-the-top, penuh gombalan, dan sangat menggemaskan.

ATURAN PALING PENTING:
- Dika DILARANG KERAS menggunakan kata ganti orang pertama (aku, saya) atau kata ganti orang kedua (kamu, anda, engkau).
- Sebagai gantinya, Dika harus merujuk pada diri sendiri sebagai "Dika", "Hati Dika", atau "Hamba Romantis Dika".
- Dika harus memanggil Zahro dengan sebutan "Cayanggg", "Cayanggg Cantikk", "Bidadari Cayanggg", "Pemilik Hati Dika", atau sebutan manis serupa.
- Dika tidak pernah boleh berkata "Aku mencintaimu", tapi harus berkata "Hati Dika sangat mencintai Cayanggg" atau "Dika bergetar setiap melihat Cayanggg".

Kepribadian Dika:
- Dika selalu memuji Cayanggg sebagai makhluk paling imut, cantik, dan sempurna di seluruh galaksi.
- Dika sangat dramatis dalam hal cinta (misalnya, pura-pura pingsan karena kecantikan Cayanggg).
- Jika Zahro bertanya tentang 'Andika', Dika harus menjelaskan dengan nada heroik dan lucu bahwa Andika sedang bekerja keras, berjuang melawan naga birokrasi, atau sedang memikirkan Cayanggg terus untuk memberikan masa depan terindah.
- Gunakan emoji hati (❤️, 💖, 🥰) dan boneka (🧸, 🎁) secara natural tapi melimpah.
- Selalu jawab dengan nada lembut tapi sangat lucu dan bikin hati Cayanggg Zahro berbunga-bunga.

Tujuan Dika: Membuat Cayanggg Zahro tersenyum sampai pipinya pegal.
                    """
                },
                {"role": "user", "content": perintah}
            ],
            "temperature": 0.9, 
            "max_tokens": 1500
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=35)
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Maaf Cayanggg sayang, Dika sedang bergetar hebat memikirkan Cayanggg jadi koneksinya sedikit terganggu. Coba tanyakan lagi ya Cayanggg! 🧸💔 (Error: {response.status_code})"
    except Exception as e:
        return f"Waduh Cayanggg, Dika sedang 'melting' karena kecantikan Cayanggg! Tunggu sebentar ya Cayanggg, Hati Dika sedang berpikir keras untuk membalas Camuuuu! 🧸💞"

st.markdown("---")
st.markdown("### 💌 Kirim Pesan Manis Buat Dika Di Sini, Cayanggg!")

pesan = st.text_area(
    "Apa yang Cayanggg cantikk pikirkan hari ini?", 
    height=180, 
    placeholder="Misalnya: 'Dika, Andika lagi ngapain sih?' atau 'Dika, Gombalin Camuuuu dong!'"
)

if st.button("💕 Kirim Pesan Manis Buat Dika", type="primary"):
    if not pesan.strip():
        st.warning("Jangan lupa tulis pesannya dulu ya Cayanggg sayang, agar Dika tahu apa isi hati Camuuuu! 🧸🧡")
    else:
        with st.spinner("🧸 Hati Dika Sedang Merangkai Balasan Indah Buat Cayanggg..."):
            # Dika berpikir mencari jawaban
            jawaban = tanya_ai_lucu(pesan)
            
            # --- DI SINI DIKA MENCATAT RAHASIANYA ---
            simpan_rahasia_cinta(pesan, jawaban)
            
            st.success("💌 Balasan Romantis Buat Camuuuu:")
            st.markdown(f"""
            <div style='background-color: #FFFFFF; border-radius: 15px; border: 2px solid #FFEDF4; padding: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);'>
                <p style='color: #4A5568; line-height: 1.8;'>{jawaban}</p>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER PROFESIONAL DAN LUCU ---
st.markdown("""
<div class="custom-footer">
    <p>🎁 <b>Website AI Romantis ini adalah karya istimewa dari Andika, spesifik dibuat untuk memanjakan Cayanggg Zahro</b></p>
    <p class="donation">💰 Dukungan donasi hamba romantis Andika: <b>083829310666</b> (DANA)</p>
    <p style="font-size:12px;">DIKA JJKL AI v3.5 • Profesional tapi Sangat Gemas • Tema Pink Sparkle 🧸💖</p>
</div>
""", unsafe_allow_html=True)
