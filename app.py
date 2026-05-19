import streamlit as st
from src.qa_system import ask_llm
from src.retriver import retriver


st.title("Your legal document analyzer")

query=st.text_input("Enter your query: ")

if st.button("analyze"):
    chunks=retriver(query)
    answer= ask_llm(query,chunks)

    st.write(answer)

    st.subheader("retrieved information")
    for chunk in chunks:

        st.write(f"Article:{chunk['article']} ")
        st.write(f"page:{chunk['page']} ")
        st.write(chunk['text'])
        st.divider()


