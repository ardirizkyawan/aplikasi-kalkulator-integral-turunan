import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi simbol
x = sp.Symbol('x')

# Judul dan Deskripsi Aplikasi
st.title("📘 Kalkulator Integral dan Turunan")
st.markdown("""
Aplikasi ini digunakan untuk menghitung **turunan** dan **integral** dari fungsi aljabar sederhana, 
serta menampilkan grafik dan penjelasan konsep secara interaktif.
""")

# Sidebar Input
st.sidebar.header("🔢 Masukkan Fungsi")
fungsi_input = st.sidebar.text_input("Masukkan fungsi f(x):", "x**2 + 3*x - 5")
operasi = st.sidebar.radio("Pilih Operasi:", ["Turunan", "Integral Tak Tentu", "Integral Tentu"])

# Batas jika Integral Tentu
if operasi == "Integral Tentu":
    a = st.sidebar.number_input("Batas bawah a:", value=0.0)
    b = st.sidebar.number_input("Batas atas b:", value=1.0)

# Proses dan Tampilkan Hasil
try:
    f = sp.sympify(fungsi_input)
    st.markdown("### ✏️ Fungsi Aljabar:")
    st.latex(f"f(x) = {sp.latex(f)}")

    if operasi == "Turunan":
        turunan = sp.diff(f, x)
        st.markdown("### ✅ Hasil Turunan:")
        st.latex(f"f'(x) = {sp.latex(turunan)}")

    elif operasi == "Integral Tak Tentu":
        integral = sp.integrate(f, x)
        st.markdown("### ✅ Hasil Integral Tak Tentu:")
        st.latex(f"\\int f(x)\\,dx = {sp.latex(integral)} + C")

    elif operasi == "Integral Tentu":
        hasil_integral = sp.integrate(f, (x, a, b))
        st.markdown(f"### ✅ Hasil Integral Tentu dari x = {a} hingga x = {b}:")
        st.latex(f"\\int_{{{a}}}^{{{b}}} f(x)\\,dx = {sp.latex(hasil_integral)}")

    # Grafik Fungsi
    st.markdown("### 📈 Grafik Fungsi")
    f_np = sp.lambdify(x, f, "numpy")
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f_np(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"f(x) = {fungsi_input}")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Grafik f(x)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

except Exception as e:
    st.error(f"Terjadi kesalahan dalam memproses fungsi: {e}")

# Penjelasan Konsep (Edukatif)
st.markdown("---")
st.markdown("## 📚 Penjelasan Konsep")

st.markdown("### 🔹 Turunan (Derivatif)")
st.write("""
Turunan menyatakan laju perubahan suatu fungsi terhadap variabel bebasnya. Dalam kehidupan nyata,
turunan digunakan untuk mengetahui kecepatan, percepatan, atau pertumbuhan.
""")
st.latex("f'(x) = \\lim_{h \\to 0} \\frac{f(x + h) - f(x)}{h}")

st.markdown("### 🔹 Integral")
st.write("""
Integral digunakan untuk menghitung akumulasi, seperti luas area di bawah kurva, total jarak, 
atau total biaya. Terdapat dua jenis:
- **Integral Tak Tentu**: menghasilkan fungsi asli dari turunan
- **Integral Tentu**: menghitung nilai total fungsi dalam interval [a, b]
""")
st.latex("\\int f(x)\\,dx = F(x) + C")
st.latex("\\int_a^b f(x)\\,dx = F(b) - F(a)")
