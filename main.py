import speech_recognition as sr
import streamlit as st
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."

def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    words = [word.lower() for word in words if word.lower() not in stopwords.words('english') and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

def chatbot(input_text=None):
    if input_text is None:
        # If input_text is not provided, use speech recognition
        input_text = transcribe_speech()

    # Preprocess the input text
    question = preprocess(input_text)

    # Return a predefined answer or default response
    # Modify this logic based on your requirements
    if question == ['hello']:
        response = "Hello! How can I help you?"
    else:
        response = "I'm sorry, but I don't have the information you're looking for."

    return response

def main():
    st.title("Chatbot")
    st.write("Hello! I'm a chatbot.")

    input_method = st.radio("Choose your input method:", ("Speech Input", "Text Input"))

    if input_method == "Speech Input":
        text = transcribe_speech()
        if text:
            response = chatbot(text)
            st.write("You: " + text)
            st.write("Chatbot: " + response)
    else:
        question = st.text_input("You:")
        if st.button("Submit"):
            response = chatbot(question)
            st.write("You: " + question)
            st.write("Chatbot: " + response)

if __name__ == "__main__":
    main()
