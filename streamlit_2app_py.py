import streamlit as st
import openai
import os
from dotenv import load_dotenv  # ADD THIS

# Load environment variables
load_dotenv()  # ADD THIS

# CORRECTED VARIABLE NAME (you had OPEMAI)
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("🚀 YOUR AI SALES AGENT")  # REMOVED #
st.subheader("Paste LinkedIn URL below")

linkedin_url = st.text_input("", value="https://www.linkedin.com/in/saleswithdhruvtomar/")
generate_clicked = st.button("Create Personalized Email")

if generate_clicked and linkedin_url:
    try:
        # Extract username from URL
        username = linkedin_url.split('/in/')[-1].split('/')[0]
        
        # CORRECTED PROMPT (removed extra " and fixed variable)
        prompt = f"""
        Create a personalized sales email for {username} using their LinkedIn profile: {linkedin_url}.
        Structure:
        1. Subject line with personal hook
        2. Compliment based on their career
        3. Value proposition related to their role
        4. Clear CTA for next steps
        """
        
        # CORRECTED MODEL NAME AND SYNTAX
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # WAS opt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],  # FIXED BRACKETS
            max_tokens=350
        )
        
        email_draft = response.choices[0].message.content
        
        st.success("AI PERSONALIZED DRAFT GENERATED!")
        st.markdown(f"**Profile:** [{username}]({linkedin_url})")
        st.text_area("Email Draft", value=email_draft, height=300)  # ADDED VALUE
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
elif generate_clicked:
    st.warning("Please enter a LinkedIn URL")
