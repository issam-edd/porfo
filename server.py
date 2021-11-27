from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)
    

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\nemail: {email},\nsubject: {subject},\nmessage: {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_write= csv.writer(database2, delimiter=';',quotechar='"', lineterminator='\n',quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'test test'