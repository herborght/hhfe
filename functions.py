import streamlit as st
import openai


@st.cache_data
def general_gpt(prompt: str):
    # make chat gpt completion function with streamlit
    openai.api_key = st.secrets["openai"]["api_key"]
    openai.api_type = "azure"
    openai.api_base = "https://cog-fxpoc-tonality-dev-01.openai.azure.com/"
    openai.api_version = "2023-03-15-preview"
    gpt_model = "gpt-4"
    completion = openai.ChatCompletion.create(
        deployment_id=gpt_model,
        messages=[
            {
                "role": "user",
                "content": "{}".format(prompt),
            }
        ],
        temperature=0.2,
        max_tokens=1500,
        top_p=1.0,
        frequency_penalty=0.1,
        presence_penalty=0.1,
    )
    return str(completion.choices[0].message.content)
