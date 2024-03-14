import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

st.set_page_config(page_title="Text-to-Speech Demo", page_icon="📈")

def get_user_input():
    user_input = st.text_input("Enter your text:")
    return user_input

def translate_text(text, dest_language):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_language)
        return translation.text
    except Exception as e:
        st.error(f"Translation error: {e}")
        return None

def speak_text(text, lang_code):
    if text:
        
        tts = gTTS(text=text, lang=lang_code, slow=False)
        tts.save("output.mp3")
        # os.system("start output.mp3")

def main():
    st.title("Translator App")

    user_input = get_user_input()
    
    # Choose destination language
    dest_language = st.selectbox("Select Destination Language:", ["Nepali", "Spanish", "French", "German"])
    lang_codes = {"Nepali": "ne", "Spanish": "es", "French": "fr", "German": "de"}
    
    if user_input:
        st.subheader("Translation Result:")
        st.write(f"Original Input: {user_input}")

        # Perform translation based on selected language
        translated_output = translate_text(user_input, lang_codes[dest_language])
        if translated_output is not None:
            st.write(f"{dest_language} Output: {translated_output}")
            speak_text(translated_output, lang_codes[dest_language])
            st.audio("output.mp3", format="audio/mp3")
        else:
            st.error("Translation failed. Please try again.")
    else:
        st.info("Enter text above for translation.")

if __name__ == "__main__":
    main()
