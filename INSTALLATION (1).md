#  Installation Guide – LocalAid Project

This guide provides step-by-step instructions for setting up the LocalAid web application on your local machine for development and testing.

---

##  Prerequisites

Ensure you have the following tools installed:

- [Python 3.8 or later](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/) – Python package installer
- [Git](https://git-scm.com/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/) *(recommended for isolating environments)*

---

##  Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/WSU-4110/LocalAid-App.git
cd LocalAid-App
```

---

##  Set Up a Virtual Environment (Optional but Recommended)

This keeps dependencies isolated:

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

---

## 📦 Install Dependencies

If a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

If not, you can manually install Flask and common dependencies:

```bash
pip install flask
```

You may also need:

```bash
pip install pytest
```

---

##  Run the Application Locally

Locate the file that runs the Flask server (e.g., `app.py`, `main.py`, or similar), then run:

```bash
python app.py
```

Or use Flask CLI:

```bash
export FLASK_APP=app.py     # On Windows: set FLASK_APP=app.py
flask run
```

Once the server starts, open your browser and go to:

```
http://127.0.0.1:5000
```

---

##  Run Unit Tests

Our team used `unittest`:

```bash
python -m unittest discover
```

This will run all test cases located in files like `test_*.py`.

---

##  Troubleshooting

| Issue                          | Solution                                                       |
|-------------------------------|----------------------------------------------------------------|
| `ModuleNotFoundError`         | Run `pip install <missing-package>`                            |
| Flask app won’t start         | Ensure you’re in the correct directory and using the right filename |
| Port already in use           | Try `flask run --port 5001`                                    |
| Virtualenv not activating     | Ensure the path is correct, or try running terminal as admin   |
