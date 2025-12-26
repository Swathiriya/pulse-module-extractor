import streamlit as st
from extractor import ModuleExtractor
from utils.validators import is_valid_url

st.set_page_config(page_title="Pulse AI Agent", layout="wide")
st.title("Pulse – Module Extraction AI Agent")

url = st.text_input("Enter documentation URL")

if st.button("Extract"):
    if not is_valid_url(url):
        st.error("Invalid URL")
    else:
        with st.spinner("Extracting modules..."):
            extractor = ModuleExtractor()
            output = extractor.extract(url)
            st.success("Extraction completed")
            st.json(output)
import streamlit as st
from extractor.extractor import ModuleExtractor
from utils.validators import is_valid_url

st.set_page_config(page_title="Pulse AI Agent", layout="wide")
st.title("Pulse – Module Extraction AI Agent")

url = st.text_input("Enter documentation URL")

if st.button("Extract"):
    if not is_valid_url(url):
        st.error("Invalid URL")
    else:
        with st.spinner("Extracting modules..."):
            extractor = ModuleExtractor()
            output = extractor.extract(url)
            st.success("Extraction completed")
            st.json(output)
