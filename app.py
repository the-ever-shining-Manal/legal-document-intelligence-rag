import streamlit as st
from src.qa_system import ask_llm
from src.retriver import retriver
from src.dashboard import dashboard_data
    
st.title("Your legal document analyzer")

query=st.text_input("Enter your query: ")
    
if st.button("analyze"):
        chunks=retriver(query)
        answer= ask_llm(query,chunks)
    
        st.write(answer)
        dashboard_st=dashboard_data(chunks)
        st.subheader("summary")
        st.markdown("## Risks")

        for item in dashboard_st:

            st.write(f"Article: {item['article']}")
            st.write(f"Page: {item['page']}")

            data = item["data"]

            st.markdown("### Risks")

            for risk in data.get("risks", []):
                st.write("-", risk)

            st.markdown("### Dates")

            for date in data.get("dates", []):
                st.write("-", date)

            st.markdown("### Stakeholders")

            for stakeholder in data.get("stakeholders", []):
                st.write("-", stakeholder)

            st.divider()
    
    
