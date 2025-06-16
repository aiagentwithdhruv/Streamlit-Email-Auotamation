import streamlit as st

st.title("🚀 YOUR AI SALES AGENT")
st.subheader("Paste LinkedIn URL below")

linkedin_url = st.text_input("")
generate_clicked = st.button("Create Personalized Email")

if generate_clicked:
    st.success("AI DRAFT GENERATED!")
    st.write("Hey [First Name], I noticed you work in [Role] at [Company]...")
    st.caption("Real AI integration coming tomorrow!")