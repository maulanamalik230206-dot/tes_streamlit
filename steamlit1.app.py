import streamlit as st

# Fungsi untuk mencari luas persegi
def luas_persegi(sisi):
    return sisi * sisi

st.title("Hitung Luas Persegi")

# Input nilai sisi persegi
s = st.number_input("Masukkan panjang sisi persegi:", min_value=0, step=1)

# Tombol untuk menghitung
if st.button("Hitung Luas"):
    luas = luas_persegi(s)
    st.success(f"Luas persegi yang Anda inginkan adalah {luas}")
