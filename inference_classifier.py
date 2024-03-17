import pickle

import cv2
import mediapipe as mp
import numpy as np

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

labels_dict = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E':'E', 'F':'F',
               'G':'G', 'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L',
               'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R',
               'S':'S', 'T':'T', 'U':'U', 'V':'V', 'W':'W', 'X':'X',
               'Y':'Y', 'Z':'Z', 'del':'Delete', 'space':'Space'}
while True:

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

    cv2.imshow('frame', frame)
    # cv2.waitKey(1)
    key = cv2.waitKey(1) & 0xFF  # Wait for 1ms and get key input
    if key == 27:  # Check if Escape key is pressed
        break


cap.release()
cv2.destroyAllWindows()

############################################################################################3
#############################################################################################

###########################################################################################
###########################################################################################

# import streamlit as st
# from streamlit_webrtc import RTCConfiguration, WebRtcMode, webrtc_streamer, VideoTransformerBase
# import cv2
# import mediapipe as mp
# import numpy as np
# import pickle
# import av

# model_dict = pickle.load(open('./model.p', 'rb'))
# model = model_dict['model']

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles

# hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# labels_dict = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4:'E', 5:'F',
#                6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L',
#                12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R',
#                18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
#                24:'Y', 25:'Z', 26:'Delete', 27:'Space'}

# # class VideoProcessor():
# #     def process(self, frame):
# #         data_aux = []
# #         x_ = []
# #         y_ = []
# #         H, W, _ = frame.shape
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert frame to RGB

# #         results = hands.process(frame_rgb)

# #         if results.multi_hand_landmarks:
# #             for hand_landmarks in results.multi_hand_landmarks:
# #                 mp_drawing.draw_landmarks(
# #                     frame_rgb,
# #                     hand_landmarks,
# #                     mp_hands.HAND_CONNECTIONS,
# #                     mp_drawing_styles.get_default_hand_landmarks_style(),
# #                     mp_drawing_styles.get_default_hand_connections_style())

# #                 # data_aux = []
# #                 for i in range(len(hand_landmarks.landmark)):
# #                     x = hand_landmarks.landmark[i].x
# #                     y = hand_landmarks.landmark[i].y
# #                     x_.append(x)
# #                     y_.append(y)
# #                     # data_aux.extend([x, y])
                
# #                 for i in range(len(hand_landmarks.landmark)):
# #                     x = hand_landmarks.landmark[i].x
# #                     y = hand_landmarks.landmark[i].y
# #                     data_aux.append(x - min(x_))
# #                     data_aux.append(y - min(y_))

# #                 x1 = int(min(x_) * W) - 10
# #                 y1 = int(min(y_) * H) - 10

# #                 x2 = int(max(x_) * W) - 10
# #                 y2 = int(max(y_) * H) - 10

# #                 prediction = model.predict([np.asarray(data_aux)])

# #                 predicted_character = labels_dict[int(prediction[0])]

# #                 # h, w, _ = frame_rgb.shape
# #                 cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
# #                 cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
# #                     cv2.LINE_AA)

# #         return frame_rgb
    

# #     def recv(self, frame):
# #         img = frame.to_ndarray(format="bgr24")
# #         img = self.process(img)
# #         return av.VideoFrame.from_ndarray(img, format="bgr24")

    

# # Streamlit app
# def main():
#     st.title("Hand Gesture Recognition")
# #     RTC_CONFIGURATION = RTCConfiguration(
# #     {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
# # )

# #     webrtc_streamer(key="example", video_processor_factory=VideoProcessor, mode=WebRtcMode.SENDRECV,
# #     rtc_configuration=RTC_CONFIGURATION,
# #     media_stream_constraints={"video": True, "audio": False},
# #     async_processing=True,)
#     cap = cv2.VideoCapture(0)
#     frame_placeholder = st.empty()
#     stop_button_pressed = st.button("Stop")
#     while cap.isOpened() and not stop_button_pressed:
#         data_aux = []
#         x_ = []
#         y_ = []

#         ret, frame = cap.read()

#         H, W, _ = frame.shape

#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         results = hands.process(frame_rgb)
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 mp_drawing.draw_landmarks(
#                     frame,
#                     hand_landmarks,
#                     mp_hands.HAND_CONNECTIONS,
#                     mp_drawing_styles.get_default_hand_landmarks_style(),
#                     mp_drawing_styles.get_default_hand_connections_style())

#             for hand_landmarks in results.multi_hand_landmarks:
#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y

#                     x_.append(x)
#                     y_.append(y)

#                 for i in range(len(hand_landmarks.landmark)):
#                     x = hand_landmarks.landmark[i].x
#                     y = hand_landmarks.landmark[i].y
#                     data_aux.append(x - min(x_))
#                     data_aux.append(y - min(y_))

#             x1 = int(min(x_) * W) - 10
#             y1 = int(min(y_) * H) - 10

#             x2 = int(max(x_) * W) - 10
#             y2 = int(max(y_) * H) - 10

#             prediction = model.predict([np.asarray(data_aux)])

#             predicted_character = labels_dict[int(prediction[0])]

#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
#             cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
#                         cv2.LINE_AA)
            
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         frame_placeholder.image(frame,channels="RGB")
#         key = cv2.waitKey(1) & 0xFF  # Wait for 1ms and get key input
#         if key == 27:  # Check if Escape key is pressed
#             break


#     cap.release()
#     cv2.destroyAllWindows()
        
    

# if __name__ == "__main__":
#     main()
