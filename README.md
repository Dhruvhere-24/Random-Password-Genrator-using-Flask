# 🔐 Random Password Generator using Flask

This is a **Random Password Generator** web app built using **Python and Flask** as part of a project for the **CodSoft Internship**.

The app generates secure random passwords based on user-specified length and allows copying them easily from the web interface.

---
**📸 Screenshot**
![Image](https://github.com/user-attachments/assets/cd8a6c51-d7a1-4d11-a79a-8510f6358089)

## 🚀 Features

- 🔑 Generate secure random passwords
- 📏 Adjustable password length
- 🖥️ Easy-to-use web interface
- 🐍 Backend powered by Python and Flask
- ❌ No JavaScript needed

---

## 📁 Folder Structure
```bash
Random-Password-Genrator-using-Flask/
│
├── static/
│ └── style.css # CSS styles for the UI
│
├── templates/
│ └── index.html # HTML template rendered by Flask
│
├── app.py # Main Flask application (Python generates password)
├── README.md # Project documentation (this file)
```

---

## 🧠 Password Generation Logic in Python

Instead of using frontend JavaScript, password generation is handled entirely by Python on the backend using the Flask framework:

- The user enters the desired password length via an HTML form.
- The backend uses Python’s `random` and `string` modules to generate the password.
- The result is displayed on the same page using Jinja2 templating.

---

## 🛠️ How to Run the Project Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dhruvhere-24/Random-Password-Genrator-using-Flask
   cd Random-Password-Genrator-using-Flask
   ```
### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
### 3. Activate the Virtual Environment
```bash

On Windows:
venv\Scripts\activate
On macOS/Linux:
```
source venv/bin/activate

4. Install Dependencies
 ```bash
pip install flask
```
6. Run the Application
```bash
python app.py
```
Then visit
```bash
📍 http://127.0.0.1:5000/ in your browser.
```
🧑‍💻 Author

- Dhruv Singh
- GitHub: @Dhruvhere-24

-------------------------------------------------------
📢 Acknowledgement

This project was completed as part of the CodSoft Internship program.
