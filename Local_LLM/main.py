import os
from langchain_community.llms import CTransformers 
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
import streamlit as st
from ctransformers import AutoModelForCausalLM


model_id = 'TheBloke/Mistral-7B-Instruct-v0.1-GGUF'
# model_id = 'TheBloke/Mistral-7B-codealpaca-lora-GGUF'
os.environ['XDG_CACHE_HOME']= './model'
config ={'temperature':0.3,'context_length': 2000}


llm = CTransformers(model = model_id,model_file="mistral-7b-instruct-v0.1.Q2_K.gguf", model_type='mistral', config=config, callbacks= [StreamingStdOutCallbackHandler()])

def fetch_conversation(query:str):

    body_json = {"who": "Who is mentioned in the query?","what": "What it is about in short? ","category": "What is the category?"}

    response = llm.invoke(f"""Provide the output in same JSON format {body_json} in markdown only:
    query : '{query}'. Provide Response in JSON only.""" )

    return response

st.header("Fetch String Context")
query = st.text_area("Enter your query",)

if st.button("Fetch"):
    with st.spinner("Fetching..."):
        response = fetch_conversation(query)
        st.write(response)
