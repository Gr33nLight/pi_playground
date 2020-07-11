from flask import Flask
from manager import Manager

app = Flask(__name__)

manager = Manager()


@app.route('/on')
def on():
    manager.on()
    return 'On'


@app.route('/off')
def off():
    manager.off()
    return 'Off'


@app.route('/blink')
def blink():
    manager.blink()
    return 'Blink'
