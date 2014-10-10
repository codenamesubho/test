#!/usr/bin/env python3

from flask import Flask, render_template, request, url_for, redirect


app= Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
             name = request.form['filename']
             ftype = request.form['type']
             return redirect(url_for('search',key='hello'))
        else:
             return redirect( url_for('search'))


@app.route('/search', methods=['GET', 'POST'])
def search():i
        if request.method=='POST':
            return 'Post data incoming'
        else:
            return 'bad test"

if __name__ == '__main__':
        app.debug = True
        app.run()
