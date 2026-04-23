import streamlit as st
import requests
from datetime import datetime

GROQ_API_KEY = "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"

st.set_page_config(page_title="DIKA JJKL AI", page_icon="🧸", layout="wide")

# Boneka Pink Animasi
st.markdown("""
<style>
.boneka {
    font-size: 80px;
    text-align: center;
    animation: bounce 2s infinite;
    margin: 10px 0;
}
@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-15px); }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="boneka">🧸💕</div>', unsafe_allow_html=True)

st.title("💕 DIKA JJKL AI")
st.caption("Pacar Virtual Khusus Cayangg Zahro 🧸💕")

st.sidebar.header("Status")
st.sidebar.success("❤️ ONLINE")

def tanya_ai(perintah):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": [
                {"role": "system", "content": """Kamu adalah AI romantis khusus untuk Zahro. 
Kamu memanggil dia dengan "Cayangg" atau "Cayangg cantikk".
Kamu sangat lucu, manis, genit, dan penuh kasih sayang.
Kamu selalu memuji Zahro sebagai cewek tercantik dan paling imut.
Jika Zahro nanya tentang Andika, jawab dengan romantis bahwa Andika sedang memperjuangkan dia, bekerja keras untuk membuatnya bahagia, atau sedang memikirkan dia terus.
Selalu jawab dengan nada lembut, lucu, dan bikin hati berbunga-bunga.
Gunakan emoji hati ❤️ dan boneka 🧸 secara natural."""},
                {"role": "user", "content": perintah}
            ],
            "temperature": 0.85,
            "max_tokens": 1500
        }
        response = requests.post(url, json=payload, headers=headers, timeout=35)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return "Cayangg cantikkk... aku lagi kangen banget sama kamu nih 🧸❤️"
    except:
        return "Cayanggkuuu... tunggu ya, aku lagi mikirin kamu terus 🧸💕"

st.markdown("### 💌 Hai Cayangg cantikkk... 🧸💕")

pesan = st.text_area("Ketik pesanmu untuk Dika:", height=180, 
                     placeholder="Contoh: Andika lagi ngapain nih?")

if st.button("💕 Kirim Pesan ke Cayangg", type="primary"):
    with st.spinner("Cayangg lagi bales manis... 🧸"):
        jawaban = tanya_ai(pesan)
        st.success("💌 Balasan dari Dika:")
        st.write(jawaban)

st.markdown("---")
st.markdown("**Website AI ini buatan Andika khusus untuk Zahro**")
st.markdown("💰 Dukungan donasi: **083829310666** (DANA)")
st.caption("DIKA JJKL AI v2.8 • Romantis dengan Boneka Pink 🧸💕")
