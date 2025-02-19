import streamlit as st 
import requests 
st.title('Real-Time Language Translation') 
# Input text 
input_text = st.text_area('Enter text to translate') 
# Language selection 
target_language = st.selectbox('Select target language', ['French', 'Spanish', 'German']) 
if st.button('Translate'): 
	 response = requests.post('http://<API_URL>/translate', json={'text': input_text}) 
	 result = response.json() 
	 st.write(f"Translated Text: {result['translated_text']}") 
