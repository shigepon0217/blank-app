import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
import os

API_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-3.2-1B"

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"]="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"
os.environ["LANGCHAIN_PROJECT"]="pr-artistic-town-49"

st.title("🎈 My new StreamLit app")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# Llamaモデルへのリクエストを送信する関数
def query_llama(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UIの設定
st.title("Llama Model - Text Generator")
input_text = st.text_area("Enter your prompt:","what is streamlit?")
button = st.button("回答を生成する")

if button:
    # Llamaにクエリを送信
    with st.spinner("Generating response..."):
        response = query_llama({
            "inputs": input_text,
        })
    
    # 生成されたテキストを表示
    st.subheader("Generated Response:")
    if 'error' in response:
        st.error(f"Error: {response['error']}")
    else:
        st.write(response[0]["generated_text"])
