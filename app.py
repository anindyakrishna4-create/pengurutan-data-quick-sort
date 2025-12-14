import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from quick_sort import quick_sort, generate_random_data

# Konfigurasi halaman Streamlit
st.set_page_config(page_title="Virtual Lab: Quick Sort", layout="wide")

# Judul dan Deskripsi
st.title("🧪 Virtual Lab: Quick Sort Interaktif")
st.markdown("""
### Visualisasi Algoritma Pengurutan Data Quick Sort
Eksperimen ini memungkinkan Anda untuk memvisualisasikan langkah-langkah algoritma Quick Sort secara interaktif. Anda dapat mengubah data dan melihat bagaimana algoritma bekerja.
""")

# Input data
size = st.sidebar.slider("Panjang Data", 5, 30, 10)
data = generate_random_data(size)

# Menampilkan data asli
st.subheader("Data Awal")
st.write(data)

# Algoritma Quick Sort
sorted_data = quick_sort(data)

# Menampilkan data yang sudah diurutkan
st.subheader("Data Setelah Diurutkan")
st.write(sorted_data)

# Menampilkan visualisasi proses pengurutan
df = pd.DataFrame({'Index': range(len(data)), 'Value': data})
df_sorted = pd.DataFrame({'Index': range(len(sorted_data)), 'Value': sorted_data})

# Grafik untuk data awal
chart = alt.Chart(df).mark_bar().encode(
    x='Index:O',
    y='Value:Q',
    color='Value:Q'
).properties(title="Data Awal")
st.altair_chart(chart, use_container_width=True)

# Grafik untuk data yang sudah diurutkan
chart_sorted = alt.Chart(df_sorted).mark_bar().encode(
    x='Index:O',
    y='Value:Q',
    color='Value:Q'
).properties(title="Data Setelah Diurutkan")
st.altair_chart(chart_sorted, use_container_width=True)

