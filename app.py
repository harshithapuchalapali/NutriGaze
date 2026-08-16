import os
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

app = Flask(__name__)
app.secret_key = 'supersecret123'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Upload folder setup
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Load trained model
MODEL_PATH = os.path.join(BASE_DIR, 'cnn_best_model.h5')
model = load_model(MODEL_PATH)
IMG_SIZE = model.input_shape[1]
CLASS_NAMES = ["Healthy", "Rotten"]

# Fake user database (in-memory)
users = {}  # email: password

# ----------------------------------------
# Helpers
# ----------------------------------------
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_image(filepath):
    try:
        img = load_img(filepath, target_size=(IMG_SIZE, IMG_SIZE))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        prediction = model.predict(img_array)
        if prediction.shape[-1] == 1:
            label = CLASS_NAMES[int(prediction[0][0] > 0.5)]
        else:
            label = CLASS_NAMES[np.argmax(prediction[0])]
        return label
    except Exception as e:
        print(f"[ERROR] Prediction failed: {e}")
        return "Prediction Error"

# ----------------------------------------
# Routes
# ----------------------------------------
@app.route('/')
@app.route('/index')
def home():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/about')
def about():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    return render_template('about.html')

@app.route('/contact')
def contact():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in users and users[email] == password:
            session['user'] = email
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not (name and email and password):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('register'))

        if email in users:
            flash('User already exists. Please login.', 'warning')
            return redirect(url_for('login'))

        users[email] = password
        session['user'] = email
        flash('Account created successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded.', 'error')
            return redirect(request.url)

        file = request.files['file']
        if not file or file.filename == '':
            flash('No selected file.', 'error')
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash('Unsupported file format. Please upload JPG or PNG.', 'error')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        result = predict_image(filepath)
        session['result'] = result
        session['filename'] = filename
        return redirect(url_for('result'))

    return render_template('predict.html')

@app.route('/result')
def result():
    if 'user' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('login'))

    result = session.get('result')
    filename = session.get('filename')
    return render_template('result.html', result=result, filename=filename)

# ----------------------------------------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
