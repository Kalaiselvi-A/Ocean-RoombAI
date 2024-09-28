import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('plastic_detector_model.h5')

# Open the webcam feed
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret:
        # Preprocess the frame for model input
        img = cv2.resize(frame, (224, 224))
        img = img.astype('float32') / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict using the model
        prediction = model.predict(img)

        # Label the frame based on prediction
        label = 'Plastic Detected' if prediction > 0.5 else 'No Plastic'
        cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the frame with the label
        cv2.imshow('Plastic Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
