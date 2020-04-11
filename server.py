"""
 Created by user in 4/6/2020

"""

from flask import Flask, render_template, request,redirect
import csv,time


def contact_logger(data):
    with open('contact_list.csv', mode='a', newline='\n') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/<string:page_name>')
def works(page_name):
    if page_name != (page_name.split('.'))[0] + '.html':
        page_name = page_name + '.html'
        print(page_name)
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submiter():
    if request.method == "POST":
        data = request.form
        contact_logger([data['name'],
              data['email'],
              data['massage']])

    return redirect('./submit_contact.html')
