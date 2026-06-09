import numpy as np
from PIL import Image
import os
from tensorflow.keras.models import load_model

ATIK_TUR_ESLESMELERI = {
    "plastik": {"kutusu": "plastik_kutu.png", "yazi": "Bu bir Plastik! Harikasın! Plastikleri geri dönüştürerek dünyamızı koruyorsun!"},
    "kağıt": {"kutusu": "kagit_kutu.png", "yazi": "Bu bir Kağıt! Ağaçları kurtarıyorsun! Harika bir iş çıkardın!"},
    "cam": {"kutusu": "cam_kutu.png", "yazi": "Bu bir Cam! Çok güzel! Camlar sonsuz kez geri dönüştürülebilir!"},
    "metal": {"kutusu": "metal_kutu.png", "yazi": "Bu bir Metal! Muhteşemsin! Metal kutuları geri dönüştürerek enerji tasarrufu yapabiliriz!"},
    "bilinmiyor": {"kutusu": "bilinmiyor_kutu.png", "yazi": "Üzgünüm, bunu tanıyamadım. Belki başka bir açıdan dener misin?"}
}

CLASS_NAMES = ["plastik", "kağıt", "cam", "metal"]
global loaded_model
loaded_model = None

try:
    if os.path.exists(MODEL_PATH):
        loaded_model = load_model(MODEL_PATH)
        print(f"Model başarıyla yüklendi: {MODEL_PATH}")
    else:
        print(f"HATA: Model dosyası bulunamadı: {MODEL_PATH}")
        print("Lütfen modelinizi doğru yola yerleştirdiğinizden emin olun.")
except Exception as e:
    print(f"Model yüklenirken bir hata oluştu: {e}")
    loaded_model = None
def tahmin_et(resim_yolu):
    if loaded_model is None:
        print("Model yüklenemediği için tahmin yapılamıyor.")
        return "bilinmiyor"
    try:
        img = Image.open(resim_yolu).convert('RGB')
        img = img.resize((224, 224)) 
        img_array = np.asarray(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = loaded_model.predict(img_array)
        tahmini_indeks = np.argmax(predictions[0])
        tahmini_tur = CLASS_NAMES[tahmini_indeks]

        print(f"Yüklenen resim: {resim_yolu}, Tahmin edilen tür: {tahmini_tur}")
        return tahmini_tur

    except Exception as e:
        print(f"Görüntü tahmin edilirken bir hata oluştu: {e}")
        return "bilinmiyor" 