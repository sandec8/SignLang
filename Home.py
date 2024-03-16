import streamlit as st

st.set_page_config(
    page_title="SignAWave - Real Time Hand Sign Recognition System",
    page_icon="👋",
    layout="centered" 
)

# Define a function to display the header
def display_header():
    st.title("SignAWave - Real Time Hand Sign Recognition System 👋")
    st.markdown(
        """
        Welcome to SignAWave - Real Time Hand Sign Recognition System! 👋

        SignAWave is a project built for Machine Learning and Data Science, specifically focusing on real-time hand sign recognition for American Sign Language (ASL). In addition to hand sign recognition, the project also includes features like text-to-speech and vice versa.

        **👈 Select a demo from the sidebar** to see some examples of what SignAWave can do!
    """
    )

# Define a function to display the about section
def display_about():
    st.markdown(
        """
        ## About SignAWave
        SignAWave is a real-time hand sign recognition system designed for American Sign Language (ASL). It uses machine learning and computer vision techniques to interpret hand gestures and translate them into text or speech. With SignAWave, users can communicate effectively using sign language in various settings.
        """
    )
    st.markdown(
        """
        SignAWave is equipped with a user-friendly interface and intuitive features, making it accessible to both beginners and experienced users. Whether you're learning ASL, teaching sign language, or simply curious about hand sign recognition technology, SignAWave offers a versatile platform for exploration and experimentation.
        """
    )

def main():
    display_header()
    display_about()

# Run the main function
if __name__ == "__main__":
    main()
