import streamlit as st

# Judul aplikasi
st.title('Aplikasi Lucu Streamlit')

# Menampilkan pesan lucu
st.header('Selamat datang di aplikasi lucu! 😄')

# Menampilkan pesan dengan emoji acak
emojis = ['😂', '🤣', '😊', '😜', '😎', '🥳']
selected_emoji = st.selectbox('Pilih emoji favoritmu!', emojis)

# Menampilkan emoji yang dipilih oleh pengguna
st.write(f'Emoji favoritmu: {selected_emoji}')

# Fungsi untuk menampilkan pesan lucu berdasarkan pilihan
def show_funny_message(emoji):
    if emoji == '😂':
        return 'Kamu lucu banget! 😂'
    elif emoji == '🤣':
        return 'Hahaha, kamu bikin ngakak! 🤣'
    elif emoji == '😊':
        return 'Wajah ceria, suka banget! 😊'
    elif emoji == '😜':
        return 'Kamu gokil deh! 😜'
    elif emoji == '😎':
        return 'Santai, keren banget! 😎'
    elif emoji == '🥳':
        return 'Ayo, kita pesta! 🥳'
    else:
        return 'Pilih emoji yang lucu ya!'

# Menampilkan pesan lucu berdasarkan emoji yang dipilih
st.subheader(show_funny_message(selected_emoji))

# Tombol untuk mengubah warna latar belakang
if st.button('Ganti warna latar belakang'):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #{selected_emoji == '😂' and 'ffcc00' or 'f0f0f0'};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
