import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyBp8TwlX6ki1Fxit8gmNhsrbbdJJFNIZfw")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config = generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])
def ans(inp,lang):
    response = convo.send_message(
        content = f"As an experienced physician with over 30 years of practice, please provide detailed information on {inp}. If {inp} refers to a medication, include essential details such as active ingredient, dosage, indications, contraindications, warnings/precautions, and side effects/adverse reactions. If {inp} denotes a medical condition, kindly elucidate the recommended all treatment options in language {lang} and ensure all the output will be in language {lang} only, covering the same critical aspects: active ingredient, dosage, indications, contraindications, warnings/precautions, and side effects/adverse reactions. Additionally, if {inp} pertains to a medical emergency, please provide immediate first aid tips and initial treatment guidelines. Your expertise and precision in delivering this information, especially in cases of emergencies, are highly valued."
        f"and fill the information and give the output in the same format")
    return response.text



# Centering logo using HTML
st.markdown("""
    <div style="display: flex; justify-content: center;">
        <img src="https://www.freepnglogos.com/uploads/medicine-logo-png-1.png" alt="Logo" width="100">
    </div>
    """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>MediSage</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>ALL THE DETAILS FOR YOUR MEDICINES</h1>", unsafe_allow_html=True)

st.write("\n\n\n")
st.markdown("<h3 style='text-align: center;'>Language</h1>", unsafe_allow_html=True)
option = st.selectbox('',
    ('English', 'Hindi',  'Nepali', 'Tamil')
)

st.markdown("<h3 style='text-align: center;'>Name of your medicine or disease</h3>", unsafe_allow_html=True)
user_input = st.text_input("")



if user_input:
    text = user_input
    with st.spinner(f'The details is being loaded for {text}'):
        x = ans(text,option)
        st.subheader(text)
        st.write(x)