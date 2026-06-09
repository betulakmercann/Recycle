import os
from flask import Flask, request, render_template, jsonify, url_for
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image 

app = Flask(__name__, static_folder='web', template_folder='web')

UPLOAD_FOLDER = 'web/uploads' 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

TUM_KUTULAR_IMAGE_FILENAME = 'tum_kutular.jpg' 
ERROR_ICON_FILENAME = 'error_icon.png'       
LOADING_SPINNER_FILENAME = 'loading_spinner.gif' 
PLACEHOLDER_BINS_FILENAME = 'placeholder_bins.png' 

MODEL_PATH = 'geri_donusum_modelim.h5' 
IMAGE_SIZE = (224, 224) 
CLASS_NAMES = ["cam", "kagit", "metal", "plastik"]

model = None
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model başarıyla yüklendi.")
except Exception as e:
    print(f"Model yüklenirken bir hata oluştu: {e}")
    print(f"Lütfen '{MODEL_PATH}' dosyasının doğru yolda ve bozuk olmadığından emin olun.")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', 
                           error_icon_path=url_for('static', filename=ERROR_ICON_FILENAME),
                           loading_spinner_path=url_for('static', filename=LOADING_SPINNER_FILENAME),
                           placeholder_bins_path=url_for('static', filename=PLACEHOLDER_BINS_FILENAME))

@app.route('/analyze', methods=['POST'])
def analyze_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400
    
    try:
        filename = secure_filename(file.filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print(f"Dosya kaydedildi: {filepath}")

        prediction_name = "Bilinmiyor" 
        feedback_message = "Bu atığı hangi kutuya atacağınızı belirleyemedik. Lütfen daha net bir resim deneyin."

        image_to_show_url = url_for('static', filename=TUM_KUTULAR_IMAGE_FILENAME)


        if model:
            try:
                img = Image.open(filepath).resize(IMAGE_SIZE)
                img_array = image.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)
                img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array) 

                predictions = model.predict(img_array)
                predicted_class_index = np.argmax(predictions[0])
                confidence = np.max(predictions[0]) * 100 
                prediction_name = CLASS_NAMES[predicted_class_index].capitalize() 
                
                if confidence > 70: 
                    feedback_message = f"Bu bir {prediction_name} atığıdır. Lütfen {prediction_name.lower()} kutusuna atmalısın."
                elif confidence > 50: 
                    feedback_message = f"Tahminimce bu bir {prediction_name} atığı. Lütfen {prediction_name.lower()} kutusuna atmalısın."
                else: 
                    feedback_message = f"Ne olduğunu tam anlayamadım, ancak en yakın tahmin {prediction_name}. Lütfen daha net bir resim deneyin."
                
            except Exception as e:
                print(f"Model tahmini sırasında hata oluştu: {e}")
                prediction_name = "Analiz Hatası"
                feedback_message = "Resim analizi sırasında bir sorun oluştu. Lütfen geçerli bir resim yüklediğinizden emin olun."
        else:
            prediction_name = "Model Yüklenemedi"
            feedback_message = "Geri dönüşüm modeli yüklenemedi. Lütfen sunucu loglarını kontrol edin."
        

        return jsonify({
            'prediction': prediction_name,
            'feedback': feedback_message,
            'image_path': image_to_show_url 
        })

    except Exception as e:
        print(f"Dosya işleme veya genel hata: {e}")
        return jsonify({'error': f'Sunucu tarafında beklenmedik bir hata oluştu: {e}'}), 500

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)