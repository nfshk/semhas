import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Congrats Shofia! ✨", page_icon="🎓", layout="centered")

# --- CUSTOM CSS (DIPERBAIKI TOTAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }

    /* Kartu Utama - Menghilangkan Animasi Floating yang bikin kotak geser */
    .gift-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-top: 10px;
    }

    .title-text {
        background: linear-gradient(to right, #ff4b4b, #ff8585);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 5px;
        text-align: center;
    }

    /* Styling Tombol agar lebih rapi */
    div.stButton > button {
        background: linear-gradient(45deg, #ff4b4b, #ff8585);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        margin-top: 20px;
    }

    /* KUNCI: Menghilangkan padding dan border bawaan Streamlit Form */
    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
    }

    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- HALAMAN 1: HOME ---
if st.session_state.page == 'home':
    st.markdown("<h1 class='title-text'>Semhastulation Shofia (u.o) S.KM 🎓</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gift-card'>
        <h2 style='color: #ff4b4b; margin-bottom: 10px;'>Proud of you, Shoff! ✨</h2>
        <p style='font-size: 1.1rem; line-height: 1.6; color: #444;'>
            <b>Kerenn bangett woyy!</b> Akhirnya menamatkan Uner ya bunddd... <br><br>
            Sebagai anak IT dan <i>Bestie GPT</i>, kali ini aku mau kasih hadiah lewat cara yang anti-mainstream nieehh. 
            Nafi si paling gas diajak kemanapun ini mau kasih hadiah semhas buat ente yaituuu...
        </p>
        <div style='background: rgba(255,255,255,0.5); padding: 15px; border-radius: 20px; margin-top: 20px;'>
            <p style='font-style:italic; color: #666; margin:0;'>
                Semoga dilancarkan revisiannya, yudisium, wisuda, dan kehidupan after kuliah ya shoff. <br>
                Semoga makin josjis kedepannyaa <br>
                Doakan juga semoga aku bisa segera menyusulll hehehe
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Lihat Hadiahnya! ✨"):
        go_to_page('gift_1')

# --- HALAMAN 2: HADIAH 1 ---
elif st.session_state.page == 'gift_1':
    st.markdown("<h2 class='title-text'>Hadiah #1: Bukber Gratis Bareng Nafii 🍜</h2>", unsafe_allow_html=True)
    
    with st.form("main_form", border=False):
        # Header dipindah ke dalam form agar tidak ada gap
        st.markdown("<p style='font-weight:600; color:#444; margin-bottom: 10px;'>Pilih tempat & waktu janjian yaa:</p>", unsafe_allow_html=True)
        
        tempat = st.radio(
            "Tempat Favorit:",
            ["Astaganaga", "Tjap Pengkol", "Ramen Ya/Suteki", "Ciamso", "Kogu"],
            horizontal=True
        )
        tanggal = st.date_input("Kapan nih?")
        catatan = st.text_area("Ada pesan yang mau disampein?", placeholder="Tulis di sini ya...")
        
        submit = st.form_submit_button("Klaim Hadiah & Lanjut ➡️")
        
        if submit:
            st.session_state.makan = tempat
            st.session_state.tgl = str(tanggal)
            st.session_state.pesan = catatan
            go_to_page('gift_2')
            
    st.markdown("</div>", unsafe_allow_html=True)

# --- HALAMAN 3: HADIAH 2 ---
elif st.session_state.page == 'gift_2':
    st.markdown("<h2 class='title-text'>Surprise Hadiah Keduaa! 📸</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='gift-card'>
        <h2 style='color: #ff4b4b; margin-bottom: 10px;'>PHOTOBOOTH TIME! 🎞️</h2>
        <p style='font-size:1.1rem; color:#444;'>Biar wacana photobooth kita terealisasi, sekalian aja jadi hadiah semhas yekann!</p>
        <p style='font-weight: bold; color: #ff4b4b; font-size: 1.3rem; margin-top:20px;'>
            Dress code: Pake baju secantik mungkin yaa! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)

    makan = st.session_state.get('makan', '-')
    tgl = st.session_state.get('tgl', '-')
    pesan_user = st.session_state.get('pesan', '-')
    
    st.info("💡 Klik tombol di bawah untuk kirim jawabanmu langsung ke email Nafi.")

    email_penerima = "nafisahikaputriherra@gmail.com"
    form_url = f"https://formsubmit.co/{email_penerima}"
    
    html_button = f"""
    <form action="{form_url}" method="POST">
        <input type="hidden" name="_subject" value="Jawaban Hadiah Semhas dari Shofia!">
        <input type="hidden" name="Tempat" value="{makan}">
        <input type="hidden" name="Tanggal" value="{tgl}">
        <input type="hidden" name="Pesan" value="{pesan_user}">
        <input type="hidden" name="_captcha" value="false">
        <button type="submit" style="
            background: linear-gradient(45deg, #ff4b4b, #ff8585);
            color: white; padding: 18px; border: none; border-radius: 50px; 
            width: 100%; cursor: pointer; font-size: 18px; font-weight: bold;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3); font-family: 'Quicksand', sans-serif;
        ">Kirim ke Nafi & Selesai! ✨</button>
    </form>
    """
    st.markdown(html_button, unsafe_allow_html=True)

    if st.button("⬅️ Kembali"):
        go_to_page('gift_1')

# --- FOOTER ---
st.markdown("<br><p style='text-align: center; color: #888; font-size:0.8rem;'>Handcrafted with ❤️ by Nafisahika</p>", unsafe_allow_html=True)

# Script auto-scroll ke atas (PENTING biar gak nyangkut di bawah)
st.components.v1.html("<script>window.parent.document.querySelector('section.main').scrollTo(0, 0);</script>", height=0)
