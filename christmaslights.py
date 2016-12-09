import serial
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    ard = serial.Serial("/dev/ttyACM0", 9600);
    msg = ard.readline();
    print(msg);

    if request.method == 'POST':
        if request.form['submit'] == 'rainbow':
            ard.write("rainbow\n")
        elif request.form['submit'] == 'strobe':
            ard.write("christmas\n")
        else:
            pass
    return render_template('index.html')
    if __name__ == "__main__":
        # lets launch our webpage!
        # do 0.0.0.0 so that we can log into this webpage
        # using another computer on the same network later
        app.run(host='0.0.0.0')
