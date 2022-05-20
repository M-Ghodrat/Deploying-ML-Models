from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb+srv://mongodb_test:mongodb_test123@cluster0.tqfx8.mongodb.net/?retryWrites=true&w=majority')

db = client.flaskapp
collection = db['users']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['fname']
        email = details['lname']
        collection.insert_one({'name': name, 'email':email})
#         return 'success'
        redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)