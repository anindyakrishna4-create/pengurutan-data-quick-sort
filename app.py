# File: app.py

import streamlit as st
import pandas as pd
import time
from quick_sort import quick_sort 
import altair as alt

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Virtual Lab: Quick Sort",
    layout="wide"
)

st.title("🧪 Virtual Lab: Quick Sort Interaktif")
st.markdown("### Visualisasi Algoritma Pengurutan Data (Pivot dan Partisi)")

st.sidebar.header("Konfigurasi Data")

# --- Input Pengguna ---
default_data = "45, 12, 90, 3, 55, 18, 70"
input_data_str = st.sidebar.text_input(
    "Masukkan data (pisahkan dengan koma):", 
    default_data
)
speed = st.sidebar.slider("Kecepatan Simulasi (detik)", 0.1, 2.0, 0.5)

# --- Proses Data Input ---
try:
    data_list = [int(x.strip()) for x in input_data_str.split(',') if x.strip()]
    initial_data = list(data_list)
except ValueError:
    st.error("Masukkan data dalam format angka yang dipisahkan oleh koma (misalnya: 10, 5, 8).")
    st.stop()
    
# --- Penjelasan ---
st.markdown("""
#### Cara Kerja Quick Sort:
Perhatikan elemen **Kuning (Pivot)**. Tujuannya adalah memindahkan semua elemen yang lebih kecil darinya ke kiri (Hijau) dan yang lebih besar ke kanan. Setelah itu, Pivot berada di posisi akhirnya (Merah).
""")

st.write(f"**Data Awal:** {initial_data}")

# --- Visualisasi Awal ---
if st.button("Mulai Simulasi Quick Sort"):
    
    sorted_data, history = quick_sort(list(data_list))
    
    st.markdown("---")
    st.subheader("Visualisasi Langkah Demi Langkah")
    
    vis_placeholder = st.empty()
    
    # --- Loop Simulasi ---
    for step, state in enumerate(history):
        current_array = state['array']
        # UNPACKING 4 ELEMEN: (start, end, pivot_idx, action_type)
        (start_range, end_range, highlight_idx, action_type) = state['highlight']
        action = state['action']

        # Membuat Dataframe untuk Visualisasi Altair
        df_vis = pd.DataFrame({
            'Index': [f'Posisi {i}' for i in range(len(current_array))],
            'Nilai': current_array,
            # Tentukan warna berdasarkan status:
            'Tipe': [
                'Pivot Aktif' if i == highlight_idx and action_type == 'Pilih Pivot' else
                'Pivot Aktif' if i == end_range and action_type in ('Bandingkan', 'Tukar') else # Tetap highlight pivot (di end_range)
                'Elemen Aktif' if i == highlight_idx and action_type in ('Tukar', 'Bandingkan') else # Highlight elemen yang sedang dilihat (j)
                'Pivot Final' if i == highlight_idx and action_type == 'Pivot Final' else
                'Normal'
                for i in range(len(current_array))
            ]
        })
        
        # --- MEMBUAT GRAFIK BATANG VERTIKAL TANPA LABEL INDEX ---
        
        chart = alt.Chart(df_vis).mark_bar().encode(
            x=alt.X('Index', 
                    sort=alt.EncodingSortField(field="Index", order='ascending'),
                    axis=None), 
            
            y=alt.Y('Nilai', scale=alt.Scale(domain=[0, max(initial_data) * 1.1])), 
            
            color=alt.Color('Tipe', 
                            scale=alt.Scale(domain=['Pivot Aktif', 'Elemen Aktif', 'Pivot Final', 'Normal'], 
                                            range=['#F1C232', '#6AA84F', '#CC0000', '#4A86E8']), # Kuning: Pivot, Hijau: Aktif, Merah: Pivot Final
                            legend=None),
            tooltip=['Index', 'Nilai', 'Tipe']
        ).properties(
            title=f"Visualisasi Quick Sort (Langkah {step+1}) | Aksi: {action_type}"
        ).interactive()

        # Tampilkan visualisasi di placeholder
        with vis_placeholder.container():
            st.altair_chart(chart, use_container_width=True)
            
            # Tampilkan status di bawah chart
            st.info(f"**Langkah ke-{step+1}** | **Aksi:** {action}")
            if action_type == 'Pivot Final':
                 st.success(f"Pivot berhasil ditempatkan. Array dibagi menjadi dua sub-array.")
            elif action_type == 'Selesai':
                 st.success("Array telah terurut! Selesai.")
            else:
                 st.caption("Kuning: Pivot. Hijau: Elemen yang sedang dibandingkan/ditukar.")


        # Jeda untuk simulasi
        time.sleep(speed)

    # --- Hasil Akhir ---
    st.balloons()
    st.success(f"**Pengurutan Selesai!**")
    st.write(f"**Data Terurut:** {sorted_data}")
    st.info(f"Algoritma Quick Sort selesai dalam **{len(history)-1}** langkah visualisasi.")
