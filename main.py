import numpy as np

from tensorflow.keras import models

from recording_helper import record_audio, terminate
from tf_helper import preprocess_audiobuffer

# !! Modify this in the correct order
#commands = ['arriba','abajo','parar','adelante','si','derecha','izquierda','no']

commands = ['abajo','adelante','arriba','derecha','izquierda','no','parar','si']
loaded_model = models.load_model("saved_model.keras")

def predict_mic():
    audio = record_audio()
    print(len(audio))
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    return command

if __name__ == "__main__":
    from turtle_helper import move_turtle
    while True:
        command = predict_mic()
        move_turtle(command)
        if command == "parar":
            terminate()
            break