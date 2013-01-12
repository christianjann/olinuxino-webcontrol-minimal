#!/usr/bin/env python
# coding=utf8

from flask import Flask, render_template, flash, request
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form,  BooleanField
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

class LedForm(Form):
    led1 = BooleanField('led1', default = bool(readpins(32)))
    led2 = BooleanField('led2', default = bool(readpins(33)))

@app.route('/', methods=('GET', 'POST',))
def index():
    form = LedForm()
    if request.method == 'POST':
        flash('LEDs have been updated: LED1="' + str(form.led1.data)
              + '", LED2="' + str(form.led2.data) +'"', 'success')
        writepins(32, int(form.led1.data))
        writepins(33, int(form.led2.data))
        return render_template('example.html', form=form)
    return render_template('example.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
