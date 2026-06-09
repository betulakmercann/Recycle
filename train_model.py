import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input 
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np
import os

DATA_DIR = 'dataset'
IMAGE_SIZE = (224, 224) 
BATCH_SIZE = 32 
EPOCHS = 50 
MODEL_SAVE_PATH = 'geri_donusum_modelim.h5' 
CLASS_NAMES = ["cam", "kagit", "metal", "plastik"]

print("--- Veri Seti Yükleniyor ---")
train_ds = image_dataset_from_directory(
    DATA_DIR,
    labels='inferred',
    label_mode='int',
    image_size=IMAGE_SIZE,
    interpolation='nearest',
    batch_size=BATCH_SIZE,
    shuffle=True, 
    seed=42
)

found_class_names = train_ds.class_names
print(f"Veri setinde bulunan sınıf isimleri: {found_class_names}")
if sorted(CLASS_NAMES) != sorted(found_class_names):
    print("UYARI: CLASS_NAMES listesi ile bulunan sınıf isimleri uyuşmuyor veya sıraları farklı.")
    print("Lütfen CLASS_NAMES listesini, dosya sistemindeki alt klasör isimlerinin alfabetik sırasına göre güncelleyin.")
    print(f"Beklenen sıra: {sorted(found_class_names)}")

num_classes = len(CLASS_NAMES)

print("\n--- MobileNetV2 Modeli Oluşturuluyor ---")
base_model = MobileNetV2(input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3),
include_top=False,
weights='imagenet')
base_model.trainable = False

preprocess_input_layer = tf.keras.layers.Lambda(preprocess_input)
input_shape=(IMAGE_SIZE[0], IMAGE_SIZE[1], 3),
name=("preprocess_input")

model = tf.keras.Sequential([
    preprocess_input_layer, 
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(), 
    tf.keras.layers.Dense(128, activation='relu'), 
    tf.keras.layers.Dropout(0.2), 
    tf.keras.layers.Dense(num_classes, activation='softmax') 
])
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("\n--- Model Özeti ---")
model.summary()

print(f"\n--- Model Eğitiliyor ({EPOCHS} Dönem) ---")
history = model.fit(train_ds, epochs=EPOCHS)

print(f"\n--- Model '{MODEL_SAVE_PATH}' olarak Kaydediliyor ---")
model.save(MODEL_SAVE_PATH)
print("Model başarıyla kaydedildi.")

print("\n--- Eğitim Tamamlandı ---")
print("Şimdi app.py dosyanızı çalıştırabilirsiniz.")