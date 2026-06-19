import streamlit as st
from sqlalchemy import create_engine

def get_engine():
    engine = create_engine(
        f"mysql+mysqlconnector://{st.secrets['user']}:{st.secrets['password']}@{st.secrets['host']}:{st.secrets['port']}/{st.secrets['database']}"
    )
    return engine