from flask import Flask, render_template, request, redirect, url_for
import base64
from requests import get
import json

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template("home.html")


@app.route('/text-to-base64')
def txtbase64en():
    return render_template("txt64in.html")


@app.route('/text-to-base64-encode', methods=['POST', 'GET'])
def b64outputen():
    if request.method == 'POST':
        b64encode = request.form['b64encode']

        encodedBytes = base64.b64encode(b64encode.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")

        return render_template('txt64out.html', encodedStr=encodedStr, b64encode=b64encode)
    else:
        return render_template('txt64in.html')


@app.route('/base64-decode')
def txtbase64de():
    return render_template("b64dein.html")


@app.route('/base64-decode-out', methods=['POST', 'GET'])
def b64outputde():
    if request.method == 'POST':
        b64decode = request.form['b64decode']
        decodedBytes = b64decode.encode("UTF-8")
        d = base64.b64decode(decodedBytes)
        decodedStr = d.decode("UTF-8")
        return render_template('b64deout.html', decodedStr=decodedStr, b64decode=b64decode)
    else:
        return render_template('b64dein.html')


@app.route('/what-is-my-ip-address')
def findmyip():
    ip = get('https://api.ipify.org').text

    yourip = format(ip)

    return render_template('findmyip.html', yourip=yourip)


@app.route('/json-validator', methods=['post', 'get'])
def jsonvalidator():
    message = ''
    if request.method == 'POST': 
        jsonvalidator = request.form['jsonvalidator']
        try:
            jsonvalidation = json.loads(jsonvalidator)
            message ="its a Valid JSON"
        except ValueError as e:
            message = "Not a Valid JSON"   
    return render_template('jsonvalidator.html', message = message)


if __name__ == "__main__":
    app.run(debug=True)
