import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="SUA_CHAVE_AQUI") 
st.write("# Chatbot de Operações de TI") 

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua solicitação (Ex: Status dos servidores)")

if texto_usuario:
    st.chat_message("user").write(texto_usuario) 
    st.session_state["lista_mensagens"].append({"role": "user", "content": texto_usuario}) 
    
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    ) 
    
    texto_resposta = resposta_ia.choices.message.content
    st.chat_message("assistant").write(texto_resposta)
    st.session_state["lista_mensagens"].append({"role": "assistant", "content": texto_resposta})
