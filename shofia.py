import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Congrats Shofia! ✨", page_icon="🎓", layout="centered")

# --- CUSTOM CSS (THE UI/UX UPGRADE) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');

    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Quicksand', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%);
    }

    /* Glassmorphism Card */
    .gift-card {
        background: rgba(255, 255, 255, 0.7);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 40px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.1);
        margin-bottom: 30px;
        animation: floating 3s ease-in-out infinite;
    }

    /* Floating Animation */
    @keyframes floating {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    /* Title Styling */
    .title-text {
        background: linear-gradient(to right, #ff4b4b, #ff8585);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 10px;
        text-align: center;
    }

    /* Button Styling */
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
    }

    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 75, 75, 0.5);
    }

    /* Info Box Styling */
    .stAlert {
        border-radius: 20px;
        background-color: rgba(255, 255, 255, 0.4);
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION LOGIC ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to_page(page_name):
    st.session_state.page = page_name

# --- PAGE 1: HOME ---
if st.session_state.page == 'home':
    st.balloons()
    st.markdown("<h1 class='title-text'>Semhastulation Shofia (u.o) S.KM🎓</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='gift-card'>
        <h2 style='color: #ff4b4b;'>Proud of you, Shoff! ✨</h2>
        <p style='font-size: 1.1rem; line-height: 1.8; color: #444;'>
            <b>Kerenn bangett woyy!</b> Akhirnya menamatkan Uner ya bunddd... <br><br>
            Sebagai anak IT dan <i>Bestie GPT</i>, kali ini aku mau kasih hadiah lewat cara yang anti-mainstream nih. 
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
    
    st.button("Lihat Hadiahnya! ✨", on_click=go_to_page, args=('gift_1',))

# --- PAGE 2: HADIAH 1 ---
elif st.session_state.page == 'gift_1':
    st.snow()
    st.markdown("<h2 class='title-text'>Hadiah #1: Bukber Gratis Bareng Nafii🍜</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='gift-card'>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight:600; color:#444;'>Pilih tempat & waktu janjian yaa:</p>", unsafe_allow_html=True)
    
    with st.form("main_form", border=False):
        tempat = st.radio(
            "Tempat Favorit:",
            ["Astaganaga", "Tjap Pengkol", "Ramen Ya/Suteki", "Ciamso", "Kogu"],
            horizontal=True
        )
        col1, col2 = st.columns(2)
        with col1:
            tanggal = st.date_input("Kapan nih?")
        with col2:
            st.write("") # Spacer
        
        catatan = st.text_area("Pesan buat Nafi (jam janjian/curhat):", placeholder="Tulis di sini ya...")
        
        submit = st.form_submit_button("Klaim Hadiah & Lanjut ➡️")
        
        if submit:
            st.session_state.makan = tempat
            st.session_state.tgl = str(tanggal)
            st.session_state.pesan = catatan
            st.session_state.page = 'gift_2'
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- PAGE 3: HADIAH 2 & KIRIM ---
elif st.session_state.page == 'gift_2':
    st.balloons()
    st.markdown("<h2 class='title-text'>Surprise Hadiah Keduaa! 📸</h2>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class='gift-card'>
        <h2 style='color: #ff4b4b;'>PHOTOBOOTH TIME! 🎞️</h2>
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
        <input type="hidden" name="Tempat Makan" value="{makan}">
        <input type="hidden" name="Tanggal" value="{tgl}">
        <input type="hidden" name="Pesan" value="{pesan_user}">
        <input type="hidden" name="_captcha" value="false">
        <button type="submit" style="
            background: linear-gradient(45deg, #ff4b4b, #ff8585);
            color: white; 
            padding: 18px; 
            border: none; 
            border-radius: 50px; 
            width: 100%;
            cursor: pointer;
            font-size: 18px;
            font-weight: bold;
            box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
            font-family: 'Quicksand', sans-serif;
        ">Kirim ke Nafi & Selesai! ✨</button>
    </form>
    """
    st.markdown(html_button, unsafe_allow_html=True)

    st.write("")
    if st.button("⬅️ Kembali"):
        go_to_page('gift_1')
        st.rerun()

# --- FOOTER ---
st.markdown("<br><p style='text-align: center; color: #888; font-size:0.8rem;'>Handcrafted with ❤️ by Nafisahika</p>", unsafe_allow_html=True)