import streamlit as st
import ollama
from typing import List, Dict
import time
import requests

# Ollama API配置
OLLAMA_API_HOST = "http://localhost:11434"
ollama.Client._base_url = OLLAMA_API_HOST

# 页面配置
st.set_page_config(page_title="本地AI聊天机器人", layout="wide")
st.title("本地AI聊天机器人")

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

# 检查Ollama服务状态
def check_ollama_service():
    try:
        response = requests.get(f"{OLLAMA_API_HOST}/api/tags")
        if response.status_code == 200:
            return True
        return False
    except requests.exceptions.RequestException:
        return False

# 获取可用模型
@st.cache_data(ttl=300)  # 缓存5分钟
def get_available_models() -> List[str]:
    if not check_ollama_service():
        st.error(f"""
        无法连接到Ollama服务。请确保：
        1. Ollama已经安装并正在运行
        2. 在终端执行 `ollama serve` 启动服务
        3. 服务地址 {OLLAMA_API_HOST} 可访问
        """)
        return ["mistral"]  # 默认模型
    
    try:
        response = requests.get(f"{OLLAMA_API_HOST}/api/tags")
        if response.status_code == 200:
            models_data = response.json()
            return [model['name'] for model in models_data['models']]
        else:
            st.warning("无法获取模型列表，使用默认模型")
            return ["mistral"]
    except Exception as e:
        st.warning(f"获取模型列表失败（将使用默认模型）: {str(e)}")
        return ["mistral"]  # 默认模型

# 检查服务状态并显示在侧边栏
with st.sidebar:
    st.title("设置")
    service_status = check_ollama_service()
    if service_status:
        st.success("✅ Ollama服务正常运行中")
    else:
        st.error("❌ Ollama服务未连接")
    selected_model = st.selectbox(
        "选择模型",
        options=get_available_models(),
        index=0
    )
    if st.button("清空对话"):
        st.session_state.messages = []
        st.rerun()

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 用户输入
user_input = st.chat_input("在这里输入您的问题...")

if user_input:
    # 添加用户消息
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 显示AI思考中的状态
    with st.chat_message("assistant"):
        with st.spinner("AI思考中..."):
            try:
                if not check_ollama_service():
                    st.error("Ollama服务未连接，请先启动服务")
                else:
                    response = ollama.chat(
                        model=selected_model,
                        messages=[{"role": m["role"], "content": m["content"]} 
                                 for m in st.session_state.messages]
                    )
                    ai_response = response["message"]["content"]
                    st.session_state.messages.append({"role": "assistant", "content": ai_response})
                    st.write(ai_response)
            except Exception as e:
                st.error(f"发生错误: {str(e)}")
