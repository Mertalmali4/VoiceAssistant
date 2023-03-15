import speech_recognition as sr
import time
import sys
from picovoice import Picovoice
from pvrecorder import PvRecorder
import time
import sqlite3
from playsound import playsound
import wikipedia
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wolframalpha
import pvporcupine
from threading import Thread
from retinaface import RetinaFace
import face_recognition
import cv2
import numpy as np





'''
def callback(recognizer, audio):                          # this is called from the background thread
    try:
        text = recognizer.recognize_google(audio, language = 'en-IN', show_all = True )
        print("I thinks you said '" + recognizer.recognize_google(audio) + "'")

        #print("You said " + recognizer.recognize_google(audio))  # received audio data, now need to recognize it
    except sr.UnknownValueError:
        print("Oops! Didn't catch that")
    except LookupError:
        print("Oops! Didn't catch that")
r = sr.Recognizer()
r.listen_in_background(sr.Microphone(), callback)

while True: time.sleep(0.1)  

'''

'''
def standby():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.6
        try:

            audio=r.listen(source,timeout=2,phrase_time_limit=7)

        except sr.WaitTimeoutError:
            return "none"
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-US")
        print(f":{query}")
    except sr.WaitTimeoutError:
        return "none"
    except Exception as e:
        return "none"
    
    

    query =query.lower()
    return query

while True:
    permission=standby()
    if("hello"in permission):
        print("okey")
    elif("bye"in permission):
        sys.exit()

'''


import pvporcupine
'''
# AccessKey obtained from Picovoice Console (https://console.picovoice.ai/)
access_key = "8fPjSJyCB9Lb/4UE8Zza3F0/XaC5cE31KbBAjAiEjiTUsbd8UX1OKw=="

handle = pvporcupine.create(access_key=access_key, keywords=['jarvis', 'bumblebee'])
'''


'''
def get_next_audio_frame():
  
  pass

while True:
  
  audio_frame = get_next_audio_frame()
  keyword_index = porcupine.process(audio_frame)
  if keyword_index >= 0:
      print("detected")
      pass
      '''
'''

def wake_word_callback():
    pass
context_path = ...  # path to Rhino context file (.RHN)
def inference_callback(inference):
    print(inference.is_understood)
    if inference.is_understood:
        print(inference.intent)
        for k, v in inference.slots.items():
            print(f"{k} : {v}")

pv = Picovoice(
    access_key={"8fPjSJyCB9Lb/4UE8Zza3F0/XaC5cE31KbBAjAiEjiTUsbd8UX1OKw=="},
    keyword_path="jarvis_en_windows_v2_1_0 -.ppn",
    wake_word_callback=wake_word_callback,
    context_path=context_path(),
    inference_callback=inference_callback)

porcupine = pvporcupine.create(
  access_key="8fPjSJyCB9Lb/4UE8Zza3F0/XaC5cE31KbBAjAiEjiTUsbd8UX1OKw==",
  keyword_paths=['jarvis_en_windows_v2_1_0 -.ppn']
)

'''
'''
import pvporcupine


for keyword in pvporcupine.KEYWORDS:
    print(keyword)








from pvrecorder import PvRecorder

porcupine = pvporcupine.create(
  access_key="8fPjSJyCB9Lb/4UE8Zza3F0/XaC5cE31KbBAjAiEjiTUsbd8UX1OKw==",
  keyword_paths=['jarvis_en_windows_v2_1_0 -.ppn'])
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)





try:
    recoder.start()
    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            print("detected")
except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()

'''

'''
#phone number location
import phonenumbers
from phonenumbers import carrier,timezone,geocoder

number = input("Telefon Numarasını  Gir: ")

if number.startswith("+"):
    print("Numara Doğru!")
    Numara = phonenumbers.parse(number)
    zaman = timezone.time_zones_for_number(Numara)
    sim_adi = carrier.name_for_number(Numara, "tr")
    bolge = geocoder.description_for_number(Numara, "tr")

    print("Saat Dilimi :", zaman)
    print("Sim adı:", sim_adi)
    print("Yaşadığı Ülke(bölge) :", bolge)

else:
    print("+ülke kodunu kullanarak giriniz.")

'''





video_capture = cv2.VideoCapture(0)
    

    

    # Load a second sample picture and learn how to recognize it.
mert_image = cv2.imread("dataset/mert.jpg")
mert_face_encoding = face_recognition.face_encodings(mert_image)[0]

    # Create arrays of known face encodings and their names
known_face_encodings = [
            
mert_face_encoding
]
known_face_names = [
    
    "Mert"
]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    
    # Grab a single frame of video
    ret, frame = video_capture.read()
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
            name = "Unknown"
            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)


    process_this_frame = not process_this_frame
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    # Display the resulting image
    cv2.imshow("Video", frame)
    # Hit 'q' on the keyboard to quit!
    if("Mert" in face_names):
        print("başarılı")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam



video_capture.release()
cv2.destroyAllWindows()
        
        
        

#a=face_recognition()






