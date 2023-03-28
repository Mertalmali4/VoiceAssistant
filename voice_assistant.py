from pvrecorder import PvRecorder
import time
from playsound import playsound
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser
import wolframalpha
import pvporcupine
from retinaface import RetinaFace
import face_recognition
import cv2
import numpy as np
import sys
import random
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.by import By
import mediapipe as mp
import mouse



class Voice_Assistant():


    
    
    


    def __init__(self):
        super().__init__()
        self.i = 0
        self.rate=180
        self.standBy()
        
        

        
    

    def speak(self,say):
        
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", self.rate) #konuşma hızı
        
        self.engine.say(say)
        self.engine.runAndWait()

    
        
    def standBy(self):
        porcupine = pvporcupine.create(
        access_key="8fPjSJyCB9Lb/4UE8Zza3F0/XaC5cE31KbBAjAiEjiTUsbd8UX1OKw==",
        keyword_paths=['jarvis_en_windows_v2_1_0 -.ppn'],
        sensitivities=[0.4])
        
        recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
        try:
            recoder.start()
            while (True):
                keyword_index = porcupine.process(recoder.read())
                if keyword_index >= 0:
                    recoder.stop()
                    
                    
                    
                    self.authentication()
                    
                    
        except KeyboardInterrupt:
            recoder.stop()
        finally:
            porcupine.delete()
            recoder.delete()



        


        
            


    def authentication(self):
        '''
        con = sqlite3.connect("user.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS USER(Name TEXT)")
        con.commit()

        
        
        self.name = "mert"
            
        i=0

        cursor.execute("insert into USER VALUES(?)",(self.name,))
        con.commit()
        
        cursor.execute("select * from USER")
        self.name = cursor.fetchall()
        '''
        a=0
        b=0
        while(1):
            self.speak("Hi. Do I know you sir?")
            self.response = sr.Recognizer()

            with sr.Microphone() as source:
                
                
                
                playsound("listeningsound.wav")
                audio = self.response.listen(source,phrase_time_limit=1.5)
            try:
                self.phrase = self.response.recognize_google(audio, language="en-US")
                self.phrase = self.phrase.lower()
                print(self.phrase)
                self.phrase= self.phrase.split(" ")
                if("administration"in self.phrase):
                    self.requests()
                if("yes" in self.phrase):
                    i=0
                    j=0
                    while(i<=1):
                        self.speak("What is your name sir?")
                        
                        with sr.Microphone() as source:
                            
                            playsound("listeningsound.wav")
                            audio = self.response.listen(source,phrase_time_limit=1.5)
                            
                        
                        try:
                            
                            self.phrase = self.response.recognize_google(audio, language="tr-TR")
                            self.phrase = self.phrase.lower()
                            self.phrase =self.phrase.split(" ")
                            print(self.phrase)
                            if("mert" in self.phrase):
                                if(i==1):
                                    self.speak("I remembered you")
                                self.face_recognition()
                            else:
                                if(i==0):
                                    self.speak("This name doesn't sound familiar, can you say it again?")
                                    i+=1
                                    continue
                                if(i==1):
                                    self.speak(f"I don't know you{self.phrase}, i go to standby")
                                    self.standBy()
                                    
                                    
                                
                        except sr.UnknownValueError:
                            
                            if(j==0):
                                self.speak("I cant hear you please talk loudly!")
                                j+=1
                                continue
                            if(j==1):
                                self.speak("You don't answer me, i go to standby")
                                self.standBy()
                            
                        
                        
                if("no"in self.phrase):
                    self.speak("I have to turn standby now ,sorry!")
                    #new member adding
                    self.standBy()
                    

                else:
                    if(a==0):
                        self.speak(" Please only say yes or no!")
                        a+=1
                        continue
                    if(a==1):
                        self.speak("You don't give the answer I want,I go to standBy")
                        self.standBy()
                    

            except sr.UnknownValueError:

                if(b==0):
                    self.speak("I cant hear you please talk loudly!")
                    b+=1
                    continue
                if(b==1):
                    self.speak("You don't answer me, i go to standby")
                    self.standBy()


    def face_recognition(self):



        
        video_capture = cv2.VideoCapture(0)
        img = cv2.imread("dataset/mert.jpg")

        resp = RetinaFace.detect_faces(img, threshold = 0.3)
        
            
        if 1==len(resp):
            for key in resp:
                identity = resp[key]
                facial_area=identity["facial_area"]
                #facial_area_location.append(((facial_area[3],facial_area[0]), (facial_area[1],facial_area[2])))
                
                
                
                crop_img = img[facial_area[1]: facial_area[3]+10, facial_area[0]: facial_area[2]+10]

                

                mert_face_encoding=face_recognition.face_encodings(crop_img)[0]

            # Load a second sample picture and learn how to recognize it.
        
        
            # Create arrays of known face encodings and their names
        known_face_encodings = [  mert_face_encoding ]
        known_face_names = [ "Mert" ]

        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        self.speak("I need to confirm you ,please look at the camera.")
        c=0
        d=0
        while c<=50:
            
            # Grab a single frame of video
            ret, frame = video_capture.read()
            # Only process every other frame of video to save time
            if process_this_frame:

                resp = RetinaFace.detect_faces(frame, threshold = 0.3)
                facial_area_location=[]
                
                if 1==len(resp):
                    for key in resp:
                        identity = resp[key]
                        facial_area=identity["facial_area"]
                        facial_area_location.append((facial_area[3],facial_area[0], facial_area[1],facial_area[2]))
                        #3012
                        crop_img = frame[facial_area[1]: facial_area[3], facial_area[0]: facial_area[2]]

                else:
                    crop_img=frame
                
                face_encodings = face_recognition.face_encodings(crop_img)
                face_names = []
                for face_encoding in face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.6)
                    name = "Unknown"
                    # # If a match was found in known_face_encodings, just use the first one.
                    # if True in matches:
                    #     first_match_index = matches.index(True)
                    #     name = known_face_names[first_match_index]
                    # Or instead, use the known face with the smallest distance to the new face
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    #if matches[best_match_index]:
                    #    name = known_face_names[best_match_index]
                    #face_names.append(name)

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                    face_names.append(name)
            
            c+=1
            process_this_frame = not process_this_frame
            if(c==50):
                self.speak("I can't see your face on camera")
                self.standBy()
            if("Mert" in face_names):
               self.greeting()
            
            if("Unknown" in face_names):
                d+=1

            if(d==6):
                cv2.imwrite("dataset/" +str(datetime)+".jpg",frame)
                self.speak("Unauthorized login procedure, I saved your pictures, don't try to login again")
                self.standBy()
                
            
        


    def greeting(self):
        hour = datetime.now().hour
        if(hour>=7 and hour<12):
            self.speak("Good Morning Sir" )
        elif(hour>=12 and hour<18):
            self.speak("Good Afternoon Sir")
        elif(hour>=18 and hour<22):
            self.speak("Good Evening sir " )
        else:
            self.speak("Good Night sir" )
        
        self.LoggedIn()
        




    def LoggedIn(self):

        self.speak("How are you today?")

        
            
        self.response = sr.Recognizer()

        with sr.Microphone() as source:
                
                
                
            playsound("listeningsound.wav")
            audio = self.response.listen(source,phrase_time_limit=5)
            try:
                self.phrase = self.response.recognize_google(audio, language="en-US")
                self.phrase = self.phrase.lower()
                print(self.phrase)
                self.phrase= self.phrase.split(" ")
                if("good" in self.phrase or "nice" in self.phrase or ("not"and "bad" in self.phrase)):
                    self.happyLogin()
                if("bad"in self.phrase or ("not"and"good" in self.phrase) or "bored" in self.phrase):
                    self.happyLogin()

            except sr.UnknownValueError:
                
                self.sadLogin()



    def happyLogin(self):
        self.speak("What can I do for you sir?")
        self.requests()

    def sadLogin(self):
        self.speak("I think you are bad today,What can I do for you sir?")
        self.requests()
        


    def mainStandBy(self):
        porcupine = pvporcupine.create(
        access_key="8fPjSJyCB9Lb/4UE8Zza3F0/XaC5cE31KbBAjAiEjiTUsbd8UX1OKw==",
        keyword_paths=['jarvis_en_windows_v2_1_0 -.ppn'],
        sensitivities=[0.4])
        
        recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
        try:
            recoder.start()
            while (True):
                keyword_index = porcupine.process(recoder.read())
                if keyword_index >= 0:
                    recoder.stop()
                    
                    self.happyLogin()
                    
                    
                    
                    
        except KeyboardInterrupt:
            recoder.stop()
        finally:
            porcupine.delete()
            recoder.delete()
        

        

    def requests(self):

        self.response = sr.Recognizer()

        with sr.Microphone() as source:
                
                
                
            playsound("listeningsound.wav")
            audio = self.response.listen(source,timeout=10,phrase_time_limit=8)
            try:
                self.phrase = self.response.recognize_google(audio, language="en-US")
                self.phrase = self.phrase.lower()
                print(self.phrase)
                self.phrase= self.phrase.split(" ")
                if("flip" in self.phrase or "flip" in self.phrase and "money" in self.phrase):
                    self.flip()
                if("joke"in self.phrase):
                    self.joke()
                if("you" in self.phrase and "fast" in self.phrase):
                    self.speak("Sorry for that I decrease the speak rate now")
                    self.rate-=10
                    self.mainStandBy()
                if("you"in self.phrase and"slow" in self.phrase):
                    self.speak("Sorry for that I increase the speak rate now")
                    self.rate+=10
                    self.mainStandBy()
                if("thank" in self.phrase and "you"in self.phrase):
                    self.speak("Your welcome")
                    self.mainStandBy()
                if("I" in self.phrase and "out" in self.phrase and "go"in self.phrase or "exit"in self.phrase):
                    self.speak("See you later ,Sir")
                    self.standBy()
                if("stop" in self.phrase or "play" in self.phrase):
                    self.stopandPlayYoutube()
                if("youtube" in self.phrase):
                    self.speak("What do you want me to open on youtube")
                    self.youtube()
                if("next" in self.phrase):
                    self.nextYoutube()
                if("close" in self.phrase and "youtube" in self.phrase):
                    self.browser.close()
                    self.mainStandBy()
                if("mouse" in self.phrase):
                    self.mouse()
                else:
                    self.speak("I don't know this words")
                    self.mainStandBy()

            except sr.UnknownValueError:
                self.speak("When you want to talk to me you can say Jarvis")
                self.mainStandBy()
            except sr.WaitTimeoutError:
                self.speak("When you want to talk to me you can say Jarvis")
                self.mainStandBy()
                
            



    def flip(self):
        options = ["tura","yazi"]
        answer = random.randint(0,1)
        a=options[answer]
        sentence = f"You got {a}"
        self.speak(sentence)
        self.requests()



    def joke(self):
        self.speak(pyjokes.get_joke())
        self.requests()
        


    def youtube(self):
        self.response = sr.Recognizer()

        with sr.Microphone() as source:
                
                
                
            playsound("listeningsound.wav")
            audio = self.response.listen(source,timeout=10,phrase_time_limit=8)
            try:
                self.phrase = self.response.recognize_google(audio, language="tr-TR")
                self.phrase = self.phrase.lower()
                
                url="https://www.youtube.com/results?search_query={}".format(self.phrase)
                self.options=webdriver.ChromeOptions()
                self.options.add_experimental_option("detach",True)
                self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
                self.browser=webdriver.Chrome(options=self.options)
                
                self.browser.get(url)
                button=self.browser.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string').click()
                self.mainStandBy()
            except sr.UnknownValueError:
                self.mainStandBy()


        
    
    def stopandPlayYoutube(self):
        button=self.browser.find_element(By.XPATH,'//*[@id="movie_player"]/div[1]/video').click()
        self.mainStandBy()
        
    def nextYoutube(self):
        button=self.browser.find_element(By.XPATH,'//*[@class="ytp-next-button ytp-button"]').click()
        self.mainStandBy()


    def mouse(self):

        mp_drawing = mp.solutions.drawing_utils
        mp_drawing_styles = mp.solutions.drawing_styles
        mp_hands = mp.solutions.hands

        ring_finger_tip=0
        index_finger_mcp=0
        index_finger_tip = 0
        middle_finger_tip=0
        thumb_tip = 0
        calibration=0
        calibrationText=0
        duration=0
        stopCount=0

        distanceHold1 = 0
        distanceHold2 = 0
        distanceHold3 = 0
        distanceClick1 = 0
        distanceClick2 = 0
        distanceClick3 = 0
        distanceStop1 = 0
        distanceStop2 = 0

        cap = cv2.VideoCapture(0)

        with mp_hands.Hands(
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.55,
            min_tracking_confidence=0.55) as hands:


            



            
            while cap.isOpened():
                calibreClick=((distanceClick2+distanceClick3)/2)
                calibreHold=((distanceHold2+distanceHold3)/2)+5
                calibreStop = ((distanceStop1+distanceStop2)/2)+4
                success, image = cap.read()
                if not success:
                    print("Ignoring empty camera frame.")
                    # If loading a video, use 'break' instead of 'continue'.
                    continue

                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                prev=time.time()
                image.flags.writeable = False
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)

                # Draw the hand annotations on the image.
            
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:
                
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
                # Flip the image horizontally for a selfie-view display.
                    cur=time.time()
                    duration+=(cur-prev)
                if not results.multi_hand_landmarks:
                    continue

                prev=time.time()
                image_height, image_width, _ = image.shape
                annotated_image = image.copy()
                
                for hand_landmarks in results.multi_hand_landmarks:
                

                    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                    index_finger_mcp= hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
                    middle_finger_tip= hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                    
                    rescaled_ring_finger_tip = (int(ring_finger_tip.x * image_width),int(ring_finger_tip.y * image_height))
                    rescaled_index_finger_tip = (int(index_finger_tip.x * image_width),int(index_finger_tip.y * image_height))
                    rescaled_thumb_tip = (int(thumb_tip.x * image_width), int(thumb_tip.y * image_height))
                    rescaled_middle_finger_tip = (int(middle_finger_tip.x * image_width), int(middle_finger_tip.y * image_height))

                    distanceStop = ((rescaled_ring_finger_tip[0] - rescaled_thumb_tip[0])**2 + (rescaled_ring_finger_tip[1] - rescaled_thumb_tip[1])**2)**0.5
                    distanceHold = ((rescaled_index_finger_tip[0] - rescaled_thumb_tip[0])**2 + (rescaled_index_finger_tip[1] - rescaled_thumb_tip[1])**2)**0.5
                    distanceClick= ((rescaled_index_finger_tip[0] - rescaled_middle_finger_tip[0])**2 + (rescaled_index_finger_tip[1] - rescaled_middle_finger_tip[1])**2)**0.5
                    
                    #x =1980-(int(index_finger_tip.x * image_width)*4)
                    
                    y=int((index_finger_mcp.y*1700)-400)
                    
                    x =2000-(int(index_finger_mcp.x * image_width)*5)
                    
                

                    if(calibration==0):

                        
                        
                        if(int(duration)==4):
                            distanceClick2=distanceClick
                        if(int(duration)==5):
                            distanceClick3=distanceClick
                        
                            calibration=1
                            calibrationText=1
                        
                            duration=0
                        duration+=0.02
                        break
                    if(calibration==1):
                        
                        
                        
                        if(int(duration)==4):
                            distanceHold2=distanceHold
                        
                        if(int(duration)==5):
                            distanceHold3=distanceHold
                        
                            calibration=2
                            calibrationText=2
                            duration=0
                        duration+=0.02
                        break
                    if(calibration==2):

                        if(int(duration)==4):
                            distanceStop1=distanceStop
                        if(int(duration)==5):
                            distanceStop2=distanceStop
                            
                            calibration=3
                        duration+=0.02
                        break
                    else:  
                        
                        
                        mouse.move(x,y,absolute=True,duration=0.02)



                        z = ((index_finger_mcp.z)*-1000)
                        
                        
                        
                        
                        if(distanceClick<calibreClick):
                            mouse.click("left")
                            
                        if(distanceHold<calibreHold):
                            mouse.hold("left")
                        if(distanceHold>calibreHold+20):
                            mouse.release("left")
                            
                        
                        if(distanceStop<calibreStop):
                            if(stopCount==10):
                                sys.exit()
                            stopCount+=1


                        
                        
                        #mouse.move(x,y,absolute=True,duration=0.07)
                        
                    
                        
                
                    

                    


                    mp_drawing.draw_landmarks(
                            annotated_image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
                    
                    cur=time.time()
                    duration+=(cur-prev)
                    duration+=0.02
                
                # Draw hand world landmarks.
                if not results.multi_hand_world_landmarks:
                    continue






                image=cv2.flip(image, 1)
                if(calibrationText==0):
                
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    seconds=int(duration)
                    cv2.putText(image,"  Please Combine Index Finger and Middle Finger",org=(30,100),fontFace=font,fontScale=0.7,color=(48,255,0),thickness=2,lineType=cv2.LINE_AA)
                    cv2.putText(image,str(seconds),org=(300,130),fontFace=font,fontScale=0.7,color=(48,255,0),thickness=2,lineType=cv2.LINE_AA)
                
                if(calibrationText==1):
                
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    seconds=int(duration)
                    cv2.putText(image,"  Please Combine Thumb and Index Finger",org=(30,100),fontFace=font,fontScale=0.7,color=(48,255,0),thickness=2,lineType=cv2.LINE_AA)
                    cv2.putText(image,str(seconds),org=(300,130),fontFace=font,fontScale=0.7,color=(48,255,0),thickness=2,lineType=cv2.LINE_AA)
                    if(int(duration)==5):calibrationText=2
                if(calibrationText==2):
                
                    font=cv2.FONT_HERSHEY_SIMPLEX
                    seconds=int(duration)
                    cv2.putText(image,"  Please Combine Thumb and Ring Finger",org=(30,100),fontFace=font,fontScale=0.7,color=(48,255,0),thickness=2,lineType=cv2.LINE_AA)
                    cv2.putText(image,str(seconds),org=(300,130),fontFace=font,fontScale=0.7,color=(48,255,0),thickness=2,lineType=cv2.LINE_AA)
                    if(int(duration)==5):calibrationText=2



                cv2.imshow('MediaPipe Hands',image )
                if cv2.waitKey(5) & 0xFF == 27:
                    break
        cap.release()

assistant = Voice_Assistant()


