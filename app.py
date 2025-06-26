from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(use_digits, use_alpha, use_special, length=12):
    chars = ''
    if use_digits:
        chars += string.digits
    if use_alpha:
        chars += string.ascii_letters
    if use_special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    if not chars:
        return 'Select at least one option'
    
    try:
        length = int(length)
        if length <= 0:
            return 'Length must be positive'
    except ValueError:
        return 'Invalid length'

    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    length = 12  # default
    if request.method == 'POST':
        use_digits = 'numberDigits' in request.form
        use_alpha = 'alphabets' in request.form
        use_special = 'specialChars' in request.form
        length = request.form.get('length', 12)
        password = generate_password(use_digits, use_alpha, use_special, length)
    return render_template('index.html', password=password, length=length)

if __name__ == '__main__':
    app.run(debug=True)
