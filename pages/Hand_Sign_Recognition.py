import streamlit as st
from streamlit_webrtc import RTCConfiguration, WebRtcMode, webrtc_streamer, VideoTransformerBase
import cv2
import mediapipe as mp
import numpy as np
import pickle


model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

labels_dict = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E':'E', 'F':'F',
               'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L',
               'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R',
               'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X',
               'Y':'Y', 'Z':'Z', 'del':'Delete', 'space':'Space'}

def main():
    st.title("Hand Gesture Recognition")
    st.write("This demo showcases real-time hand sign recognition for American Sign Language (ASL). Users can interact with their webcam to perform hand gestures, and SignAWave will recognize and display the corresponding ASL alphabet letter.")
    st.subheader("🌟 Welcome to the Hand Sign Recognition Demo !")
    st.write("Click on the Start button to enable the demo!")

    stop_button_pressed = False
    if "btnval" not in st.session_state: st.session_state.btnval = False
    def toggle_btns(): st.session_state.btnval = not st.session_state.btnval
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        start_button = col1.button('Start', on_click=toggle_btns, disabled=st.session_state.btnval)
    with col2:
        pass
    with col3:
        pass
    with col4:
        pass
    with col5:
        stop_button = col5.button('Stop', on_click=toggle_btns, disabled=not st.session_state.btnval)

    if start_button:
        if stop_button:
            stop_button_pressed = True
            cap.release()
            cv2.destroyAllWindows()
            
        cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
        while cap.isOpened() and not stop_button_pressed:
            data_aux = []
            x_ = []
            y_ = []

            ret, frame = cap.read()

            H, W, _ = frame.shape

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        frame,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        x_.append(x)
                        y_.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        data_aux.append(x - min(x_))
                        data_aux.append(y - min(y_))

                x1 = int(min(x_) * W) - 10
                y1 = int(min(y_) * H) - 10

                x2 = int(max(x_) * W) - 10
                y2 = int(max(y_) * H) - 10

                prediction = model.predict([np.asarray(data_aux)])

                predicted_character = labels_dict[prediction[0]]

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
                cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                            cv2.LINE_AA)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_placeholder.image(frame, channels="RGB")    

if __name__ == "__main__":
    main()
