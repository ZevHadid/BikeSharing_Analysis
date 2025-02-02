import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("dashboard/main_data.csv")
st.sidebar.title("Input Variabel")

nama_kolom = [kol for kol in df.columns if df[kol].dtype in ["int64", "float64"]]

kolom1 = st.sidebar.selectbox(
    "variabel 1",
    nama_kolom,
    index=8
)

kolom2 = st.sidebar.selectbox(
    "variabel 2",
    nama_kolom,
    index=14
)

var1 = df[kolom1]
var2 = df[kolom2]

st.sidebar.write(f"Korelasi antara `{kolom1}` dan `{kolom2}`: `{var1.corr(var2)}`")
st.sidebar.write(f"covariance antara `{kolom1}` dan `{kolom2}`: `{var1.cov(var2)}`")

st.title("Dashboard Penyewaan Sepeda")
st.write("## Tabel main_data.csv:")
vis_tabel = st.radio(
    "Visualisasi Tabel:",
    ["Semua Data", "groupby", "describe", "info"]
)

if vis_tabel == "Semua Data":
    st.write(df)

elif (vis_tabel == "groupby"):
    st.write(df.groupby(kolom1).agg({kolom2: ["sum", "mean", "count", "min", "max"]}))

elif (vis_tabel == "describe"):
    st.write(df.describe())

else:
    st.write(
        pd.DataFrame({
            "Nama Kolom": df.columns,
            "Jumlah Non-Null": df.count().values,
            "Tipe Data": df.dtypes.values
        })
    )

plot = ""
st.write(f"## {"Scatter Plot" if plot == "" else plot} {kolom1} dan {kolom2}")
plot = st.radio("Tipe Plot:", ["Scatter Plot", "Bar Plot"])

if plot == "Scatter Plot":
    fig, ax = plt.subplots()
    sns.scatterplot(x=var1, y=var2, ax=ax)
    st.pyplot(fig)

elif plot == "Bar Plot":
    st.write(f"## Bar Plot {kolom1} dan {kolom2}")
    fig, ax = plt.subplots()
    sns.barplot(x=kolom1, y=kolom2, data=df, ax=ax)
    st.pyplot(fig)