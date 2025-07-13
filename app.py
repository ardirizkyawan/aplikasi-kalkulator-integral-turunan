import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi simbol
t = sp.Symbol('t')

# Fungsi konsumsi air
f = -t**2 + 6*t

# Turunan (laju konsumsi)
f_prime = sp.diff(f, t)

# Titik maksimum konsumsi
t_maks = sp.solve(f_prime, t)[0]
konsumsi_maks = f.subs(t, t_maks)

# Integral tentu (total air dikonsumsi dari jam 6–12 siang)
total_konsumsi = sp.integrate(f, (t, 0, 6))

# Tampilan aplikasi
st.title("💧 Studi Kasus: Konsumsi Air Minum Harian")
st.markdown("### Fungsi Laju Konsumsi Air:")
st.latex("f(t) = -t^2 + 6t \quad \text{(liter per jam)}")

# Turunan
st.markdown("### 1️⃣ Turunan: Laju Perubahan Konsumsi Air")
st.latex("f'(t) = " + sp.latex(f_prime))

st.markdown("### 2️⃣ Waktu Konsumsi Maksimum")
st.write(f"Konsumsi maksimum terjadi pada t = {t_maks} jam setelah pukul 06.00 (yaitu pukul {6 + int(t_maks)}.00)")
st.latex(f"f({t_maks}) = {konsumsi_maks} \text{{ liter per jam}}")

# Integral tentu
st.markdown("### 3️⃣ Total Konsumsi Air dari Jam 06.00 - 12.00")
st.latex(r"\int_0^6 f(t)\,dt = " + f"{total_konsumsi} \text{{ liter}}")

# Grafik
st.markdown("### 📈 Grafik Konsumsi Air")

# Konversi ke fungsi numerik
f_np = sp.lambdify(t, f, "numpy")
f_prime_np = sp.lambdify(t, f_prime, "numpy")
t_vals = np.linspace(0, 6, 300)

fig, ax = plt.subplots()
ax.plot(t_vals, f_np(t_vals), label='f(t): Laju Konsumsi Air', color='blue')
ax.plot(t_vals, f_prime_np(t_vals), label="f'(t): Turunan", color='green', linestyle='--')
ax.axvline(x=float(t_maks), color='red', linestyle=':', label='Maksimum Konsumsi')
ax.set_xlabel("Waktu (jam sejak 06.00)")
ax.set_ylabel("Liter per Jam")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Catatan akhir
st.markdown("---")
st.info("Dengan aplikasi ini, kita dapat memahami konsep turunan & integral dalam konteks nyata, seperti pola konsumsi air sehari-hari.")
