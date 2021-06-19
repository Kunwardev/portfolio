#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 18 00:17:52 2021

@author: kunwar
"""

from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
def my_home():
    return render_template('./index.html')

@app.route('/works.html')
def my_work():
    return render_template('./works.html')

@app.route('/about.html')
def my_about():
    return render_template('./about.html')

@app.route('/contact.html')
def my_contacts():
    return render_template('./contact.html')

@app.route('/thankyou.html')
def test():
    return render_template('./thankyou.html')

def write_to_file(data):
    with open('./database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')
        
def write_to_csv(data):
    with open('./database.csv', mode='a', newline='\n') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Could not save to database'
    else:
        return 'Something went wrong'
    
if __name__ == "__main__":
    app.run(debug=True)