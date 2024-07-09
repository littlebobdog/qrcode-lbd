import streamlit as st
import spacy

# Load English tokenizer, tagger, parser, NER and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to analyze text using SpaCy
def analyze_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc]
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return tokens, entities

# Streamlit app
st.title("NLP with Streamlit")

# Input text area
input_text = st.text_area("Enter text to analyze:", height=200)

# Analyze button
if st.button("Analyze"):
    if input_text:
        st.write("Original Text:")
        st.write(input_text)
        st.write("Tokenized Text:")
        tokens, entities = analyze_text(input_text)
        st.write(tokens)
        st.write("Named Entities:")
        st.write(entities)
    else:
        st.warning("Please enter some text to analyze.")
