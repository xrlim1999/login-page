# Login Page – Flask Application

A simple Flask-based login application demonstrating user authentication with a backend database.

---

## 📌 Requirements

- Python **3.9+**
- `pip`
- `git`

---

## 📂 Project Structure
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

## 🔧 Setup (macOS)
```bash
git clone https://github.com/xrlim1999/login-page.git
cd login-page

# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the application
python main.py

## 🔧 Setup (Windows / Linux)
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

🌐 Running the Application
Once the application has started running, open the browser on your local computer and navigate to: http://127.0.0.1:5000
