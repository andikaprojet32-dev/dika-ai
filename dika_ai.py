import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime

# ================== GROQ API KEY ==================
GROQ_API_KEY = "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"

st.set_page_config(
    page_title="DIKA JJKL AI INTELLIGENCE",
    page_icon="🕵️‍♂️",
    layout="wide"
)

st.title("🕵️‍♂️ DIKA JJKL AI INTELLIGENCE")
st.markdown("**Agen Siber Khusus Polisi Siber**")
st.caption("Powered by Groq • Mode Hemat Quota")

st.sidebar.header("STATUS AGEN")
st.sidebar.success("✅ ONLINE")
st.sidebar.info(f"Waktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S WIB')}")

# ================== FUNGSI GROQ (Model Ringan) ==================
def tanya_groq(perintah):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instant",        # Model paling ringan & cepat
            "messages": [
                {"role": "system", "content": "Kamu adalah DIKA JJKL AI INTELLIGENCE. Agen siber polisi yang selalu nurut perintah. Jawab singkat tapi jelas dan akurat."},
                {"role": "user", "content": perintah}
            ],
            "temperature": 0.7,
            "max_tokens": 1200
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        elif response.status_code == 429:
            return "⚠️ Quota Groq sementara habis. Tunggu 1-2 menit lalu coba lagi."
        else:
            return f"Error Groq ({response.status_code}): {response.text[:200]}"
    except Exception as e:
        return f"Gagal koneksi: {str(e)}"

# ================== PENCARIAN WEB ==================
def cari_di_web(query):
    try:
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}+leak+OR+bocor"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(search_url, headers=headers, timeout=15)
        soup = BeautifulSoup(resp.text, 'html.parser')
        results = []
        for g in soup.find_all('div', class_='g')[:5]:
            title = g.find('h3')
            link = g.find('a')
            snippet = g.find('div', class_='VwiC3b')
            if title and link:
                results.append({
                    "Judul": title.get_text(),
                    "Link": link['href'],
                    "Snippet": snippet.get_text()[:200] if snippet else ""
                })
        return results
    except:
        return [{"Error": "Pencarian gagal"}]

# TABS
tab1, tab2 = st.tabs(["🧠 Perintah Agen", "🌐 Pencarian Web"])

with tab1:
    perintah = st.text_area("Masukkan perintah Anda:", height=160, 
                            placeholder="Contoh: Halo, siapa kamu?")
    
    if st.button("🚀 EKSEKUSI PERINTAH", type="primary"):
        with st.spinner("Agen sedang berpikir..."):
            hasil = tanya_groq(perintah)
            if "Quota" in hasil:
                st.warning(hasil)
            else:
                st.success("✅ Berhasil!")
                st.write(hasil)

with tab2:
    query = st.text_input("Keyword pencarian:", placeholder="data bocor email")
    if st.button("🔍 Cari di Web"):
        with st.spinner("Mencari..."):
            results = cari_di_web(query)
            for r in results:
                if "Error" in r:
                    st.error(r["Error"])
                else:
                    st.markdown(f"**{r['Judul']}**")
                    st.write(r['Link'])
                    st.caption(r.get('Snippet', ''))
                    st.markdown("---")

# FOOTER
st.markdown("---")
st.markdown("**Website AI ini buatan Andika**")
st.markdown("💰 Dukungan donasi: **083829310666** (DANA)")
st.caption("DIKA JJKL AI INTELLIGENCE v1.8 • Model Ringan")
