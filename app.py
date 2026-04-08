import streamlit as st
import requests

st.set_page_config(page_title="VibeCheck APAC", page_icon="🔥")

# Styling to make it look "Fancy"
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 VibeCheck APAC 2026")
st.subheader("The Cultural Sentiment Intelligence Agent")
st.markdown("---")

user_input = st.text_area("Enter slang or social media text:", placeholder="e.g., This project is lodi, petmalu!")
country = st.selectbox("Select APAC Country:", ["India", "Indonesia", "Philippines", "General"])

if st.button("Analyze Vibe 🚀"):
    if user_input:
        with st.spinner("Gemini is analyzing..."):
            backend_url = "https://vibe-check-apac-2026-476968105744.asia-east1.run.app/chat" 
            try:
                response = requests.post(backend_url, json={"text": user_input, "country": country})
                data = response.json()
                
                st.success("Analysis Complete!")
                
                # Big bold result so it's impossible to miss
                st.subheader(f"Result: {data['agent_response']}")
                st.info(f"💡 Cultural Note: {data['cultural_note']}")
                
                if "10" in data['agent_response'] or "fire" in user_input.lower():
                    st.balloons()
            except Exception as e:
                st.error(f"Connection Error: {e}")
    else:
        st.warning("Please enter some text first!")

st.sidebar.markdown("### About the Project")
st.sidebar.info("Built for GenAI Academy APAC Track 1. Powered by Gemini 1.5 Flash and Google Cloud Run.")
