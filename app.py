import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi simbol
t = sp.Symbol('t')

# Fungsi posisi
s = t**3 - 6*t**2 + 9*t

# Turunan pertama (kecepatan)
v = sp.diff(s, t)

# Turunan kedua (percepatan)
a = sp.diff(v, t)

# Judul
st.title("📌 Studi Kasus: Kalkulator Integral & Turunan")
st.markdown("### Fungsi Posisi Benda:")
st.latex("s(t) = t^3 - 6t^2 + 9t")

# Menampilkan turunan pertama dan kedua
st.markdown("### 1️⃣ Kecepatan (Turunan Pertama):")
st.latex(f"v(t) = s'(t) = {sp.latex(v)}")

st.markdown("### 2️⃣ Percepatan (Turunan Kedua):")
st.latex(f"a(t) = v'(t) = {sp.latex(a)}")

# Integral tentu (perpindahan)
st.markdown("### 3️⃣ Integral Tentu: Perpindahan dari t = 0 sampai t = 3")
jarak = sp.integrate(s, (t, 0, 3))
st.latex(r"\int_0^3 s(t)\,dt = " + f"{sp.latex(jarak)} \text{{ meter}}")

# Grafik fungsi
st.markdown("### 📊 Visualisasi Fungsi")

# Konversi fungsi ke bentuk numerik
f_pos = sp.lambdify(t, s, 'numpy')
f_vel = sp.lambdify(t, v, 'numpy')
f_acc = sp.lambdify(t, a, 'numpy')

# Nilai x untuk grafik
t_vals = np.linspace(0, 5, 400)

fig, ax = plt.subplots(3, 1, figsize=(6, 10))

# Grafik posisi
ax[0].plot(t_vals, f_pos(t_vals), color='blue')
ax[0].set_title('Fungsi Posisi s(t)')
ax[0].grid(True)

# Grafik kecepatan
ax[1].plot(t_vals, f_vel(t_vals), color='green')
ax[1].set_title('Fungsi Kecepatan v(t)')
ax[1].grid(True)

# Grafik percepatan
ax[2].plot(t_vals, f_acc(t_vals), color='red')
ax[2].set_title('Fungsi Percepatan a(t)')
ax[2].grid(True)

plt.tight_layout()
st.pyplot(fig)

# Penjelasan tambahan
st.markdown("---")
st.markdown("✅ Aplikasi ini menunjukkan bagaimana konsep turunan dan integral diterapkan untuk menganalisis gerak benda dalam konteks matematika terapan.")
