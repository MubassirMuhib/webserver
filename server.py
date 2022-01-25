from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def default_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def file_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        name = data["name"]
        email = data["email"]
        message = data["message"]

        # you just have to memorize this next two lines
        csv_writer = csv.writer(database, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
# we have to write action= "submit_form" in action section in the form area which is in the html file
# also method="post" must be added in the form beside action also in the html file
# 'GET' means that the browser wants us to sent information. 'POST' means browser wants us to save information
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            file_to_csv(data)
            return redirect('/message_accepted.html')
        except:
            return 'Did not save to the database'
    else:
        return 'Something went wrong. Try again'
