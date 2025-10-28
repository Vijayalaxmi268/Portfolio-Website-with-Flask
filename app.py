from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Normally you would save or send this info via email
    flash(f"Thank you {name}! Your message has been received.", "success")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
