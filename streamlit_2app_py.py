import streamlit as st
import openai
import os

# Securely load API key from environment
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("🚀 YOUR AI SALES AGENT")
st.subheader("Paste LinkedIn URL below")

linkedin_url = st.text_input("", value="https://www.linkedin.com/in/saleswithdhruvtomar/")
generate_clicked = st.button("Create Personalized Email")

if generate_clicked and linkedin_url:
    try:
        # Extract username from URL
        username = linkedin_url.split('/in/')[-1].split('/')[0]
        
        prompt = f"""
        Create a personalized sales email for {username} using their LinkedIn profile: {linkedin_url}.
        Structure:
        1. Subject line with personal hook
        2. Compliment based on their career
        3. Value proposition related to their role
        4. Clear CTA for next steps
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350
        )
        
        email_draft = response.choices[0].message.content
        
        st.success("AI PERSONALIZED DRAFT GENERATED!")
        st.markdown(f"**Profile:** [{username}]({linkedin_url})")
        st.text_area("Email Draft", email_draft, height=300)
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
elif generate_clicked:
    st.warning("Please enter a LinkedIn URL")
