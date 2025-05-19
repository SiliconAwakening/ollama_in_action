import streamlit as st
import ollama

# Ollama API配置
OLLAMA_API_HOST = "http://localhost:11434"
ollama.Client._base_url = OLLAMA_API_HOST

st.title("本地AI聊天机器人")
user_input = st.text_input("问我任何问题：")

if user_input:
    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response["message"]["content"])