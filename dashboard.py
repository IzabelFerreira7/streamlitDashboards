import pandas as pd 
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown("# Análise de Vendas de Mercado")
st.write("Primeira analise de dados usando streamlit")
st.write("01/05/2024")

st.markdown("## Introdução")
st.write("Aqui é um detalhamento sobre o projeto ")

st.header("DASHBOARD")

df = pd.read_csv("supermarket_sales.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City",
                  title="Faturamento por dia")
col1.plotly_chart(fig_date,  use_container_width=True)

fig_prod = px.bar(df_filtered, x="Total", y="Product line",
                   color="City",title="Faturamento por tipo de produto", orientation="h")
col2.plotly_chart(fig_prod,  use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total",
                  title="Faturamento for Filial")
col3.plotly_chart(fig_city,  use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                  title="Faturamento por Pagamento")
col4.plotly_chart(fig_kind,  use_container_width=True)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, x="City", y="Rating",
                  title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)
