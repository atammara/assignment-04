import streamlit as st
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# App title and config
st.set_page_config(layout="wide")
st.title("🌍 Country Information Explorer")

# Sample country data (in production, use an API like RestCountries)
COUNTRIES = {
    "USA": {
        "capital": "Washington, D.C.",
        "population": "331 million",
        "language": "English",
        "currency": "USD",
        "flag_url": "https://flagcdn.com/w320/us.png"
    },
    "Japan": {
        "capital": "Tokyo",
        "population": "126 million",
        "language": "Japanese",
        "currency": "JPY",
        "flag_url": "https://flagcdn.com/w320/jp.png"
    },
    "Germany": {
        "capital": "Berlin",
        "population": "83 million",
        "language": "German",
        "currency": "EUR",
        "flag_url": "https://flagcdn.com/w320/de.png"
    },
    "Brazil": {
        "capital": "Brasília",
        "population": "213 million",
        "language": "Portuguese",
        "currency": "BRL",
        "flag_url": "https://flagcdn.com/w320/br.png"
    }
}

# Sidebar filters
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select countries:",
    options=list(COUNTRIES.keys()),
    default=list(COUNTRIES.keys())
)

# Display country cards
cols = st.columns(2)  # 2-column layout

for i, country in enumerate(selected_countries):
    data = COUNTRIES[country]
    
    with cols[i % 2]:  # Alternate between columns
        with st.container(border=True):
            # Header with flag and name
            col1, col2 = st.columns([1, 3])
            with col1:
                try:
                    response = requests.get(data["flag_url"])
                    flag_img = Image.open(BytesIO(response.content))
                    st.image(flag_img, width=100)
                except:
                    st.warning("Couldn't load flag")
            
            with col2:
                st.markdown(f"## {country}")
            
            # Country details
            st.divider()
            st.markdown(f"""
            **Capital:** {data["capital"]}  
            **Population:** {data["population"]}  
            **Language:** {data["language"]}  
            **Currency:** {data["currency"]}
            """)
            
            # Interactive element
            with st.expander("More info"):
                st.write(f"Showing additional details about {country}...")
                # In a real app, add more API data here

# Add new country form
with st.expander("Add Custom Country"):
    with st.form("new_country"):
        name = st.text_input("Country Name")
        capital = st.text_input("Capital")
        population = st.text_input("Population")
        language = st.text_input("Official Language")
        currency = st.text_input("Currency")
        flag_url = st.text_input("Flag Image URL")
        
        if st.form_submit_button("Add Country"):
            if name:
                COUNTRIES[name] = {
                    "capital": capital,
                    "population": population,
                    "language": language,
                    "currency": currency,
                    "flag_url": flag_url
                }
                st.success(f"Added {name}!")
                st.rerun()