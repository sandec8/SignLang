from googletrans import Translator
from gtts import gTTS
import os

def get_user_input():
    user_input = input("Enter your text: ")
    return user_input

def translate_to_nepali(text):
    translator = Translator()
    try:
        translation = translator.translate(text, dest='ne')
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def speak_nepali(text):
    if text:
        tts = gTTS(text=text, lang='ne', slow=False)
        tts.save("output.mp3")
        os.system("start output.mp3")

def main():
    user_input = get_user_input()
    nepali_output = translate_to_nepali(user_input)

    if nepali_output is not None:
        print("\nOriginal Input: {}".format(user_input))
        print("Nepali Output: {}".format(nepali_output))
        speak_nepali(nepali_output)
    else:
        print("Translation failed. Please try again.")

if __name__ == "__main__":
    main()
