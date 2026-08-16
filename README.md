# 🍎 NutriGaze — Fresh vs Rotten Fruit Classification

NutriGaze is a deep learning web application that identifies whether a fruit is **fresh (healthy)** or **rotten** by analyzing an uploaded image. It combines a convolutional neural network (CNN) trained with TensorFlow with a responsive Flask web interface, making the classification available directly in the browser.

> Accuracy: **97%** · Stack: **Python, Flask, TensorFlow, OpenCV**

---

## ✨ Features

- **AI-powered classification** — a CNN model (`cnn_best_model.h5`) classifies fruit as `Healthy` or `Rotten`.
- **Image upload & prediction** — upload a JPG/PNG and get an instant result.
- **User authentication** — register / login / logout with session-based access control.
- **Secure uploads** — file type validation and safe filename handling via `werkzeug`.
- **Responsive interface** — clean, mobile-friendly pages built with the Flask templating engine.
- **Extensible model input** — automatically adapts to the trained model's input size.

---

## 🏗️ Tech Stack

| Layer       | Technology                                   |
| ----------- | -------------------------------------------- |
| Backend     | Python 3, Flask (+ sessions, flash messages) |
| ML / AI     | TensorFlow / Keras (CNN), OpenCV, NumPy      |
| Frontend    | HTML, CSS, JavaScript (Flask templates)      |
| Utilities   | Pillow, scikit-learn, pandas                 |

---

## 📁 Project Structure

```
NutriGaze/
├── app.py                  # Flask application (routes, auth, prediction)
├── rotten_detector.ipynb   # CNN training & evaluation notebook
├── cnn_best_model.h5       # Trained CNN model
├── Requirements.txt        # Python dependencies
├── templates/              # HTML pages (login, register, predict, result, ...)
├── static/                 # CSS & JS assets
├── uploads/                # Uploaded images (auto-created)
├── document/               # Project documentation
└── vedio demo/             # Demo videos
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harshithapuchalapali/NutriGaze.git
cd NutriGaze
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / macOS
```

### 3. Install dependencies

```bash
pip install -r Requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open **http://127.0.0.1:5000** in your browser, register an account, and upload a fruit image to get a prediction.

---

## 🧠 How It Works

1. **Training (notebook):** `rotten_detector.ipynb` trains a CNN model on fresh vs. rotten fruit images and exports the best-performing weights to `cnn_best_model.h5`.
2. **Prediction pipeline:** uploaded images are resized to the model's input size, normalized (`/255.0`), and passed through the model.
3. **Classification:** the output is mapped to either `Healthy` or `Rotten` based on the predicted probability.
4. **UI flow:** `predict` → `result`, with all pages protected behind login.

> 💡 The app lays out an extensible user system, so swapping the in-memory `users` dict for a real database is straightforward.

---

## 📄 API / Routes

| Route        | Method       | Description                            |
| ------------ | ------------ | -------------------------------------- |
| `/`          | GET          | Home page (login required)             |
| `/register`  | GET / POST   | Create an account                      |
| `/login`     | GET / POST   | Sign in                                |
| `/logout`    | GET          | Sign out                               |
| `/predict`   | GET / POST   | Upload an image and run prediction     |
| `/result`    | GET          | Show the classification result         |

---

## ✅ Supported Image Formats

- JPG / JPEG
- PNG

---

## 🛠️ Dependencies

```
tensorflow>=2.0
keras>=2.3.0
pandas
scikit-learn
opencv-python
numpy
Pillow
```

---

## 🔮 Future Enhancements

- Return **confidence score** (%) alongside the predicted label.
- Support classification across **multiple fruit classes** and other food items.
- Replace the in-memory user store with a **database-backed auth system** (e.g., SQLite/Supabase).
- Dockerize the app for easier deployment.

---

## 📜 License

This project is for educational purposes. Feel free to use and modify it with attribution.

---

## 👩‍💻 Author

**Harshitha Puchalapalli**  
[GitHub](https://github.com/harshithapuchalapali) · [LinkedIn](https://linkedin.com/in/harshitha-puchalapalli)
