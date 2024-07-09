import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

# Load pre-trained translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-jap"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Function to translate text
def translate(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    # Perform translation
    outputs = model.generate(**inputs)
    # Decode the translated text
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translated_text

# Streamlit app
st.title('Japanese to English Translation App')

# Input text area
input_text = st.text_area("Enter Japanese text to translate:", height=200)

# Translate button
if st.button('Translate'):
    if input_text:
        st.write("Original Japanese Text:")
        st.write(input_text)
        st.write("Translated English Text:")
        translated = translate(input_text)
        st.write(translated)
    else:
        st.warning("Please enter some text to translate.")
