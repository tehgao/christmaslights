import serial
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    ard = serial.Serial("/dev/ttyACM0", 9600);
    msg = ard.readline();

    if request.method == 'POST':
        if request.form['submit'] == 'rainbow':
            ard.write("rainbow\n")
        elif request.form['submit'] == 'strobe':
            ard.write("christmas")
        else:
            pass
