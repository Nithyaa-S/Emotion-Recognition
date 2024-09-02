 Emotion-Recognition

The project aims to develop a system that can capture facial expressions in real time and 
classify them into predefined categories such as happy, sad, angry, and surprised. This 
system integrates computer vision techniques with machine learning models to achieve its 
functionality. 

Workflow: 
• Capture: The system uses a webcam to capture live video of the user's face. 
• Detect: Mediapipe, a framework for building multimodal applied machine learning 
pipelines, is utilized to detect facial landmarks from the captured video frames. 
• Classify: A neural network model, trained using TensorFlow/Keras, processes the 
detected landmarks and classifies the facial expressions into predefined categories. 
• Display: The results, including the recognized facial expressions, are displayed on 
a user-friendly interface in real time. 

 User Interface

 Components: 
• Live Video Feed: This component displays the webcam feed in real-time, allowing 
the user to see their own face as the system processes it. 
• Landmark Overlay: Detected facial landmarks are overlaid on the live video feed 
to visually indicate the points being analyzed by the system. 
• Expression Label: The recognized facial expression is displayed on the screen, 
providing immediate feedback to the user. 
 HTML: Used to structure the web page and its elements, creating a clear and logical 
layout for the user interface. 
• CSS: Employed to style the web page, enhancing its visual appeal and making it 
user-friendly.

User Interaction: 
• Start/Stop Capture: Buttons are provided to start and stop the video feed, giving 
the user control over when the system should begin or cease processing. 
• Results Display: The recognized facial expression is updated in real time, ensuring 
that the user receives immediate and continuous feedback.

Snapshots

Home Page 
![Screenshot 2024-07-26 120632](https://github.com/user-attachments/assets/2af65900-f494-48f0-8be0-83edb3eb090c)


Fetch image Page:

![Screenshot 2024-07-26 124418](https://github.com/user-attachments/assets/48665f11-5741-487a-96f4-7fc369fd8a81)


Output Image 
![Screenshot 2024-09-01 123629](https://github.com/user-attachments/assets/b8c7d5db-7259-458e-af34-2b95031b4529)
