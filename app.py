from langchain_openai import OpenAI
import streamlit as st
import os

from dotenv import load_dotenv

load_dotenv() ## to load  the environment varaibles

print(os.getenv("OPENAI_API_KEY"))
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),temperature=0.5)
    response=llm(question)
    return response


st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key='input')

response=get_openai_response(input)

submit=st.button("Ask the Question")

if submit:
    st.subheader("The Response is")
    st.write(response)