import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Streamlit App")
st.title("This is a title")

st.write("""
# This is a first-level heading
## This is a second-level heading
Hello, this is my first web app. I thought its the same as webpage but I guess I'm wrong!
""")

st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))
