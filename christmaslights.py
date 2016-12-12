import serial
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
ard = serial.Serial("/dev/ttyACM0", 9600);
table = serial.Serial("/dev/ttyACM1", 9600);
msg = ard.readline();
print(msg);

@app.route('/', methods = ['POST','GET'])
def index():
    return render_template('index.html')
    if __name__ == "__main__":
        # lets launch our webpage!
        # do 0.0.0.0 so that we can log into this webpage
        # using another computer on the same network later
        app.run(host='0.0.0.0')

@app.route('/christmas/<cmd>')
def xmaslights(cmd):
    if cmd == "rainbow":
        ard.write("rainbow\n")
    elif cmd == "christmas":
        ard.write("christmas\n")
    elif cmd == "off":
        ard.write("off\n");
    else:
        pass

    return "Wrote %s to christmas lights" % cmd

@app.route('/table/<cmd>')
def coffeetable(cmd):
    if cmd == "cycle":
        table.write("cycle\n")
    elif cmd == "breathe":
        table.write("breathe\n")
    elif cmd == "off":
        table.write("off");
    else:
        pass

    return "Wrote %s to coffee table" % cmd;
