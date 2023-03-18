import cv2
import mediapipe as mp
import mouse


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

index_finger_mcp=0
index_finger_tip = 0
middle_finger_tip=0
thumb_tip = 0
distance = 0
y_axis=0
sensitivity=3
j=0


cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.55,
    min_tracking_confidence=0.55) as hands:
  
    

    
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
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
    
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      

      index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
      thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
      index_finger_mcp= hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
      middle_finger_tip= hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
      
      rescaled_index_finger_tip = (int(index_finger_tip.x * image_width),int(index_finger_tip.y * image_height))
      rescaled_thumb_tip = (int(thumb_tip.x * image_width), int(thumb_tip.y * image_height))
      rescaled_middle_finger_tip = (int(middle_finger_tip.x * image_width), int(middle_finger_tip.y * image_height))

      distance = ((rescaled_index_finger_tip[0] - rescaled_thumb_tip[0])**2 + (rescaled_index_finger_tip[1] - rescaled_thumb_tip[1])**2)**0.5
      distanceclick= ((rescaled_index_finger_tip[0] - rescaled_middle_finger_tip[0])**2 + (rescaled_index_finger_tip[1] - rescaled_middle_finger_tip[1])**2)**0.5
      
      #x =1980-(int(index_finger_tip.x * image_width)*4)
      
      y=int((index_finger_mcp.y*1700)-280)
      
      x =2000-(int(index_finger_mcp.x * image_width)*5)
      
      

      '''
      if((y_axis-y)<=0):
        if((y_axis-y)==0):
          a=mouse.get_position()
          a=a[1]
        a=mouse.get_position()
        a=a[1]+((y-y_axis)*sensitivity)
        y_axis=y
      
      else:
        a=mouse.get_position()
        a=a[1]-((y+y_axis)*sensitivity)
        y_axis=y

      '''
      mouse.move(x,y,absolute=True,duration=0.02)



      z = ((index_finger_mcp.z)*-100)
      print(distance,z)

      
      if(z>=5):
        if(distanceclick<26):
          mouse.click("left")
            
        if(distance<27):
          mouse.hold("left")
          break
        if(distance>40):
          mouse.release("left")
      if(z>=3):
        
        if(distanceclick<26):
          mouse.click("left")
            
        if(distance<27):
          mouse.hold("left")
          break
        if(distance>40):
          mouse.release("left")
      if(z>=1):
        
        if(distanceclick<22):
          mouse.click("left")
            
        if(distance<24):
          mouse.hold("left")
          break
        if(distance>35):
          mouse.release("left")
      if(z<=1):
        
        if(distanceclick<22):
          mouse.click("left")
            
        if(distance<24):
          mouse.hold("left")
          break
        if(distance>35):
          mouse.release("left")
       
      



      
      
      #mouse.move(x,y,absolute=True,duration=0.07)
      
      
          
    
      

      


      mp_drawing.draw_landmarks(
          annotated_image,
          hand_landmarks,
          mp_hands.HAND_CONNECTIONS,
          mp_drawing_styles.get_default_hand_landmarks_style(),
          mp_drawing_styles.get_default_hand_connections_style())
    
    # Draw hand world landmarks.
    if not results.multi_hand_world_landmarks:
      continue







    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()





