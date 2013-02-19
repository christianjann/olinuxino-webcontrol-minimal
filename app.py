#!/usr/bin/env python
# coding=utf8

from flask import Flask, render_template, flash, request, redirect, url_for
from flask.ext.bootstrap import Bootstrap
from leds import *

# init gpio's
export_pins(32)
setpindirection(32, "out")
export_pins(33)
setpindirection(33, "out")

app = Flask(__name__)
Bootstrap(app)

app.config['BOOTSTRAP_USE_MINIFIED'] = True
app.config['BOOTSTRAP_USE_CDN'] = True
app.config['BOOTSTRAP_FONTAWESOME'] = True
app.config['SECRET_KEY'] = 'devkey'


@app.route('/')
def index():
    in_out = {'led1': bool(readpins(32)), 'led2': bool(readpins(33))}
    return render_template('example.html', in_out=in_out)


@app.route('/set_leds', methods=('GET', 'POST',))
def set_leds():
    if request.method == 'POST':
        led1 = bool(request.form.get('led1'))
        led2 = bool(request.form.get('led2'))
        print("led1: ", led1)
        print("led2: ", led2)
        flash('LEDs have been updated: LED1="' + str(led1)
              + '", LED2="' + str(led2) + '"', 'success')
        writepins(32, int(led1))
        writepins(33, int(led2))
    return redirect(url_for('index'))

if __name__ == '__main__':
    # '0.0.0.0': listen on all public IPs
    app.run(host='0.0.0.0', port=5000, debug=True)
