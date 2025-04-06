import streamlit as st
from weather_scraper import get_weather_data
import pandas as pd

st.set_page_config(page_title="Live Weather App", page_icon="⛅", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4e8bed;'>🌦️ Selenium Powered Weather Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Get live weather data for any city in the world</p>", unsafe_allow_html=True)
st.markdown("---")

location = st.text_input("📍 Enter any location in India", placeholder="e.g., Mumbai, Jaipur, Bengaluru")

if st.button("🔍 Get Weather"):
    if location.strip() == "":
        st.warning("⚠️ Please enter a valid location.")
    else:
        with st.spinner("🔄 Fetching live weather data..."):
            RESULT = get_weather_data(location)

        st.subheader(f"🌡️ Temperature Overview for **{location.title()}**")
        col1, col2, col3 = st.columns(3)

        col1.metric(label="Current Temperature", value=f"{RESULT['current_temp']} 🌡️")
        col2.metric(label="Feels Like", value=f"{RESULT['feels_like_temp']} 🧥")
        col3.metric(label="Min/Max Temp", value=f"{RESULT.get('low_temp')} / {RESULT.get('high_temp')}")

        st.markdown(f"<h3 style='text-align: center; color: #555;'>{RESULT['weather_quickie']}</h3>", unsafe_allow_html=True)

        st.markdown("---")

        st.subheader("📊 Additional Weather Info")
        card_cols = st.columns(3)

        for i, card in enumerate(RESULT['cards']):
            with card_cols[i % 3]:
                st.info(f"**{card['title']}**\n\n{card['body']}", icon="📌")

        st.markdown("---")

        table_params = [val['param'].upper() for val in RESULT['additional_data']]
        table_values = [val['value'] for val in RESULT['additional_data']]
        table = pd.DataFrame({
            'PARAMETERS': table_params,
            'VALUES': table_values
        })

        st.subheader("📋 Detailed Weather Parameters")
        st.dataframe(table, use_container_width=True)
