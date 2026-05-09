import streamlit as st
from google import genai
import time

# Konfigurasi Halaman
st.set_page_config(page_title="SuperGen AI", layout="wide")
st.title("🚀 SuperGen: Apapun Bisa Jadi Nyata")

# Sidebar untuk API Key (Agar aman)
with st.sidebar:
    api_key = st.text_input("Gemini API Key", type="password")
    mode = st.radio("Pilih Mode:", ["Generate Video (Veo 3.1)", "Tanya Apapun (Gemini)"])

if not api_key:
    st.warning("Masukkan API Key dari Google AI Studio untuk memulai!")
else:
    client = genai.Client(api_key=api_key)
    prompt = st.text_area("Masukkan perintah kamu di sini...")

    if st.button("Proses Sekarang"):
        if mode == "Generate Video (Veo 3.1)":
            with st.spinner("Veo 3 sedang merender videomu..."):
                # Memanggil API Veo 3.1 Lite
                operation = client.models.generate_videos(
                    model="veo-3.1-lite-preview",
                    prompt=prompt,
                )
                # Menunggu hingga selesai
                while not operation.done:
                    time.sleep(5)
                
                # Tampilkan hasil
                st.video(operation.result.video_uri)
                st.success("Video berhasil dibuat!")
        
        else:
            with st.spinner("Berpikir..."):
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=prompt
                )
                st.markdown(response.text)