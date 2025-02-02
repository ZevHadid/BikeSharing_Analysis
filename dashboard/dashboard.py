import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

day_df = pd.read_csv("dashboard/main_data.csv")

st.title("Analisis Penyewaan Sepeda")

st.header("1. Pengaruh Suhu terhadap Penyewaan Sepeda")

fig, ax = plt.subplots()
sns.regplot(x=day_df['temp'], y=day_df['cnt'], ax=ax, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
ax.set_xlabel("Temperature (Normalized)")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Hubungan Suhu dan Jumlah Penyewaan Sepeda")
st.pyplot(fig)

# Heatmap korelasi
st.subheader("Heatmap Korelasi")
fig, ax = plt.subplots()
corr = day_df[['temp', 'cnt']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.write("Dari scatter plot dan heatmap, kita bisa melihat bahwa ada korelasi positif antara suhu dan jumlah penyewaan sepeda. Ini berarti saat suhu meningkat, jumlah penyewaan sepeda juga cenderung meningkat.")

st.header("2. Pengaruh Hari Kerja terhadap Penyewaan Sepeda")

fig, ax = plt.subplots()
avg_cnt_by_workingday = day_df.groupby("workingday")["cnt"].mean()
sns.barplot(x=avg_cnt_by_workingday.index, y=avg_cnt_by_workingday.values, ax=ax)
ax.set_xticks([0, 1])
ax.set_xticklabels(["Libur", "Hari Kerja"])
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Perbandingan Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
st.pyplot(fig)

st.subheader("Perbandingan Registered vs Casual")
fig, ax = plt.subplots()
day_grouped = day_df.groupby("workingday")[["registered", "casual"]].mean()
day_grouped.plot(kind='bar', stacked=True, ax=ax)
ax.set_xticklabels(["Libur", "Hari Kerja"], rotation=0)
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Registered vs Casual pada Hari Kerja dan Hari Libur")
st.pyplot(fig)

st.write("Dari grafik di atas, terlihat bahwa jumlah pengguna registered meningkat signifikan pada hari kerja, sedangkan jumlah casual menurun. Ini menunjukkan bahwa pada hari kerja, kebanyakan pengguna adalah pelanggan tetap (commuters), sementara pada hari libur lebih banyak orang menyewa sepeda untuk rekreasi.")
