# Login Page – Flask Application

A simple Flask-based login application featuring user authentication using the following setups:
- frontend: HTML
- backend: Flask
- data storage: local database

---

## 📌 Requirements

- Python **3.9+**
- `pip`
- `git`

---

## 📂 Project Structure
```bash
login-page/
├── main.py
├── requirements.txt
├── README.md
├── website/
│ ├── __init__.py
│ ├── views.py
│ ├── auth.py
│ ├── models.py
│ ├── constants.py
│ ├── templates/
│ │ ├── base.html
│ │ ├── home.html
│ │ ├── dashboard.html
│ │ ├── register.html
│ │ ├── login.html
```

## 🔧 Setup (macOS)
```bash
git clone https://github.com/xrlim1999/login-page.git
cd login-page

# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip3 install -r requirements.txt

# run the application
python3 main.py
```

## 🔧 Setup (Windows / Linux)
```bash
git clone https://github.com/xrlim1999/login-page.git
cd login-page

# create virtual environment
python -m venv venv

# activate virtual environment
# Windows (PowerShell)
venv\Scripts\activate
# Linux
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the application
python main.py
```

## 🌐 Running the Application
Once the application has started running, open the browser 
on your local computer and navigate to URL: http://127.0.0.1:5000

---

## Implemented features

- User registration, login, and logout
- Password securely hashed using Werkzeug (pbkdf2:sha256) and verification
- Session management

---

## Generative AI usage

- Generative AI (ChatGPT) was utilised to assist in debugging, environment setup,
  git setup, and documentation.
- All implementation logic and final code decisions were made by the Author with
  help and inspirations from online tutorials

---