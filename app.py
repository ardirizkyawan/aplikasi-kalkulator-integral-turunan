import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi simbol
t = sp.Symbol('t')

# Fungsi konsumsi air (liter per jam)
f = -t**2 + 6*t
f_prime = sp.diff(f, t)

# Titik maksimum konsumsi
t_maks = sp.solve(f_prime, t)[0]
konsumsi_maks = f.subs(t, t_maks)

# Integral tentu: total konsumsi dari jam 6 pagi (t=0) sampai 12 siang (t=6)
total_konsumsi = sp.integrate(f, (t, 0, 6))

# Judul dan Deskripsi
st.title("💧 Studi Kasus: Konsumsi Air Minum Harian")
st.markdown("""
Aplikasi ini menganalisis konsumsi air seseorang dari jam 06.00 hingga 12.00 menggunakan konsep turunan dan integral. 
Model matematika: \( f(t) = -t^2 + 6t \)
""")

# Layout dua kolom untuk input dan hasil
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Fungsi Konsumsi Air")
    st.latex("f(t) = -t^2 + 6t")
    st.markdown("\( t \): waktu (jam setelah pukul 06.00)\n\n\( f(t) \): laju konsumsi air (liter per jam)")

with col2:
    st.subheader("🧮 Perhitungan")
    st.markdown("### Turunan")
    st.latex(f"f'(t) = {sp.latex(f_prime)}")
    st.markdown(f"Konsumsi maksimum terjadi pada \( t = {t_maks} \), yaitu pukul **{6 + int(t_maks)}.00**")
    st.latex(f"f({t_maks}) = {konsumsi_maks} \\ \text{{ liter/jam}}")

    st.markdown("### Integral Tentu")
    st.latex(r"\int_0^6 f(t)\,dt = " + f"{sp.latex(total_konsumsi)} \\ \text{{ liter}}")

# Grafik
st.subheader("📊 Grafik Konsumsi Air")
f_np = sp.lambdify(t, f, "numpy")
f_prime_np = sp.lambdify(t, f_prime, "numpy")
t_vals = np.linspace(0, 6, 300)

fig, ax = plt.subplots()
ax.plot(t_vals, f_np(t_vals), label="f(t): Laju Konsumsi", color='blue')
ax.plot(t_vals, f_prime_np(t_vals), label="f'(t): Turunan", color='green', linestyle='--')
ax.axvline(float(t_maks), color='red', linestyle=':', label='Puncak Konsumsi')
ax.set_xlabel("Waktu (jam setelah 06.00)")
ax.set_ylabel("Liter per jam")
ax.grid(True)
ax.legend()
st.pyplot(fig)

# Penjelasan Konsep
st.markdown("---")
st.markdown("## 📚 Penjelasan Konsep")

st.markdown("### 🔹 Turunan (Derivatif)")
st.write("""
Turunan menunjukkan laju perubahan fungsi terhadap waktu. Dalam studi ini, turunan digunakan untuk mengetahui 
kapan konsumsi air mencapai puncaknya.
""")
st.latex("f'(t) = \\lim_{h \to 0} \\frac{f(t + h) - f(t)}{h}")

st.markdown("### 🔹 Integral")
st.write("""
Integral digunakan untuk menghitung total akumulasi air yang diminum dalam kurun waktu tertentu.
""")
st.latex("\\int_a^b f(t)\\,dt = F(b) - F(a)")
st.markdown("Dalam kasus ini, dari jam 06.00 sampai 12.00, total konsumsi adalah **36 liter**.")
