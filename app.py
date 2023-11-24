import streamlit as st
import pandas as pd
import numpy as np
import openai
from functions import general_gpt

st.title("HH Fire Eater")

prompt_string = """I have a room with length {} and width {}. 
I have these requirements: 
- maximum distance between two nozzles is 7.32 m 
- maximum distance from the wall to a nozzle is 3.66 m

Where is the optimal placement of nozzles in the room when I want to minimize the use of nozzles? 

The answer should contain the placement of nozzles, and the number of nozzles needed. 
""".format(
    8, 4.8
)
with st.form("gpt_form"):
    text = st.text_area("ChatGPT Prompt", prompt_string, height=200)

    submitted = st.form_submit_button("Submit")
    if submitted:
        output = general_gpt(text)

if submitted:
    st.write(output)
