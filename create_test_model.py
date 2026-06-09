import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input
MODEL_SAVE_PATH = 'geri_donusum_modelim.h5'

def create_and_save_simple_model():
    model = Sequential([
        Input(shape=(224, 224, 3)), 
        Flatten(), 
        Dense(128, activation='relu'), 
        Dense(4, activation='softmax') 
    ])

    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.save(MODEL_SAVE_PATH)
    print(f"Basit test modeli '{MODEL_SAVE_PATH}' başarıyla oluşturuldu ve kaydedildi.")

if __name__ == '__main__':
    create_and_save_simple_model()