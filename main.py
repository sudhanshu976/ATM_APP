from flask import Flask, render_template, redirect, url_for
import subprocess
app = Flask(__name__)

@app.route('/')
def home():
    subprocess.Popen(["streamlit", "run", "app.py"])
    return redirect(url_for("home"))

@app.route('/streamlit1')
def streamlit1():
    pass
    # Run your first Streamlit app using a subprocess


@app.route('/streamlit2')
def streamlit2():
    # Run your second Streamlit app using a subprocess
    subprocess.Popen(["streamlit", "run", "deposit.py"])
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)