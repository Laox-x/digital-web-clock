# ⏰ Digital Web Clock

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A modern, lightweight, and clean **web-based digital clock** built using **Python** and **Flask**.

---

## 🚀 Features

- Real-time digital clock
- Modern and responsive design
- Lightweight Flask backend
- Easy installation
- Cross-platform support (Windows & Linux)

---

## 📦 Requirements

- Python 3.9 or higher
- Git
- pip

---

# 🛠 Installation

---

## 🖥 Windows Installation

```bash
cd Desktop
git clone https://github.com/Laox-x/digital-web-clock.git
cd digital-web-clock

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Upgrade pip (recommended)
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

---

## 🐧 Linux Installation

```bash
cd ~/Desktop
git clone https://github.com/Laox-x/digital-web-clock.git
cd digital-web-clock

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip (recommended)
python3 -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

---

# ▶️ Running the Project

---

## 🖥 Windows

```bash
venv\Scripts\activate
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

Or:

```bash
venv\Scripts\activate
python app.py
```

---

## 🐧 Linux

```bash
source venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Or:

```bash
source venv/bin/activate
python3 app.py
```

---

## 🌐 Access the Application

After running the project, open your browser and go to:

```
http://127.0.0.1:5000
```

---

# 📁 Project Structure

```
digital-web-clock/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
└── README.md
```

---

# 🧠 How It Works

The project uses:

- **Flask** as a lightweight web framework
- HTML/CSS for frontend design
- JavaScript for real-time clock updates
- Python backend to serve the application

---

# 📌 Development Mode

To enable debug mode manually:

Windows:
```bash
set FLASK_DEBUG=1
```

Linux:
```bash
export FLASK_DEBUG=1
```

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Laox-x**

---

# ⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub.

---

# 📬 Contact

For suggestions or improvements, feel free to open an issue or pull request.
