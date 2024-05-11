import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="HR Recruitment Expert System",
    page_icon=":clipboard:",
    layout="wide"
)

# Set RIA Money Transfer color scheme
primary_color = "#F15A24"
secondary_color = "#0074C8"
background_color = "#FFFFFF"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background-color: {background_color};
    }}
    .sidebar .sidebar-content {{
        background-color: {primary_color};
        color: white;
    }}
    .Widget .content {{
        color: {primary_color};
    }}
    .stButton button {{
        background-color: {secondary_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.title("HR Recruitment Expert System")

# Load company logo
logo = Image.open(""C:\Users\Sadmam Sobhan\Desktop\Academic Project\Ria_Main_Logo_Descriptor_Color_RGB.png"")
st.image(logo, use_column_width=True)

# Main content
st.header("Vetting the Hiring Process")
st.write("This application helps in vetting the hiring process of RIA Money Exchange.")

# Add your content and functionality here

# Footer
st.markdown("---")
st.write("RIA Money Exchange")
