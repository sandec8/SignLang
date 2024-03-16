import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from langdetect import detect 
import pycountry
import pyttsx3 

all_languages = ('en')
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def getLangName(lang_code):
    language = pycountry.languages.get(alpha_2 = lang_code)
    return language.name

def takecommand():
    st.markdown("### 🎙️ Speak your sentence:")
    with st.empty():
        st.write("")

        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.empty().write("🎤 Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        st.empty().write("🔍 Recognizing...")

    try:
        query = r.recognize_google(audio, language='en-in')
        st.write("🗣️ You said:")
        st.text_area(label="original-text", value=query, disabled=True)
    except Exception as e:
        st.write("🔈 Say that again, please...")
        return "None"

    return query

def main():
    st.title("Speech-to-Text Translator App")
    st.subheader("🌟 Welcome to the translator demo!")
    st.write("This demo allows users to speak a speech, and SignAWave will convert it into text in the English language.")
    st.write("Click on Translate button below to get started!")

    if st.button("Translate"):
        query = takecommand()

        while query == "None":
            query = takecommand()

        from_lang = detect(query)
        lang_name = f'... {getLangName(from_lang)}'
        st.markdown(f"🔤 The user's sentence is in {lang_name}")

        translator = Translator()
        translated_text = translator.translate(query, dest='en').text

        # Display translated text
        st.write("🔁 Translated Text:")
        st.text_area(label="translated-text", value=translated_text, disabled=True)


if __name__ == "__main__":
    main()
