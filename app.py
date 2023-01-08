from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from ADFGVX import ADFGVX_encrypt, ADFGVX_decrypt

app = Flask(__name__)
app.secret_key = 'super secret'
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encrypt():
    text = request.form['text']
    key = request.form['key']
    column_key = request.form['column_key']
    result = ADFGVX_encrypt(text, key, column_key)
    return jsonify(result)

@app.route('/decode', methods=['POST'])
def decrypt():
    text = request.form['text']
    key = request.form['key']
    column_key = request.form['column_key']
    result = ADFGVX_decrypt(key, text, column_key)
    return jsonify(result)

if __name__ == '__main__':
    app.run()